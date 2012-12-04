from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from imagekit.models import ImageModel
import os, datetime

GENDER = (
    (u'Male', u'Male'),
    (u'Female', u'Female'),
)

MARITAL_STATUS = (
	(u'Single', u'Single'),
	(u'Married', u'Married'),
	(u'Widowed', u'Widowed'),
)

TAX_STATUS = (
	(u'Z',u'Z'),
	(u'S/ME',u'S/ME'),
	(u'ME1/S1',u'ME1/S1'),
	(u'ME2/S2',u'ME2/S2'),
	(u'ME3/S3',u'ME3/S3'),
	(u'ME4/S4',u'ME4/S4'),
	(u'Exempted',u'Exempted'),
)

def upload_to(instance, filename):
    name, dot, ext = filename.rpartition('.')
    name = "{0}.{1}".format(instance.user.username, ext)
    return os.path.join('profiles', name)

class DepartmentManager(models.Manager):
	def get_by_natural_key(self, acronym):
		return self.get(acronym=acronym)

class Department(models.Model):
	name = models.CharField("Name", max_length=120, unique=True)
	acronym = models.CharField("Acronym",max_length=10, unique=True)
	
	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created By")
	last_updated = models.DateTimeField(blank=True, null=True)
	
	objects = DepartmentManager()
	
	def save(self, *args, **kwargs):
		self.last_updated = datetime.datetime.now()
		super(Department, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.name

class DesignationManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class Designation(models.Model):
	name = models.CharField("Name", max_length=120, unique=True)
	department = models.ForeignKey(Department, verbose_name="Department")
	
	created = models.DateTimeField(default=datetime.datetime.now())
	last_updated = models.DateTimeField(default=datetime.datetime.now())
	
	objects = DesignationManager()
	
	class Meta:
		unique_together = ('name','department')
	
	def save(self, *args, **kwargs):
		self.last_updated = datetime.datetime.now()
		super(Designation, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class UserProfileManager(models.Manager):
	def get_by_natural_key(self, username):
		return self.get(user__username=username)

class UserProfile(ImageModel):
    user  = models.OneToOneField(User, verbose_name="User")
    bio   = models.TextField("About Me", blank=True, null=True)
    image = models.ImageField("Photo", upload_to=upload_to, storage=settings.UPLOAD_STORAGE, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(verbose_name="Gender", max_length=6, choices=GENDER, blank=True, null=True)
    marital_status = models.CharField(verbose_name="Marital Status", max_length=20, choices=MARITAL_STATUS, blank=True, null=True)
    
    # better a foreign key to some predefined lists
    city = models.CharField("City", max_length=30, blank=True, null=True)    
    country = models.CharField("Country", max_length=30, blank=True, null=True, default="Philippines")
    
    personnel_id = models.PositiveIntegerField(default=0, unique=True, blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    official_email = models.EmailField(unique=True, blank=True, null=True)
    
    tax_status = models.CharField("Tax Status", max_length=10, blank=True, null=True, choices=TAX_STATUS)
    
    objects = UserProfileManager()
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
    class IKOptions:
        spec_module = 'core.specs'
        image_field = 'image'    
        cache_dir   = 'cache'
    
    def __unicode__(self):
        return u"{0}'s profile".format(self.user.username)

    @property
    def fullname(self):
        return self.user.get_full_name()
    
    @property
    def get_fullname(self):
        return u"{0}, {1}".format(self.user.last_name, self.user.first_name)
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25  )
    
    @property
    def location(self):
        if self.city and self.country:
            return "{0}, {1}".format(self.city, self.country)
        else:
            return None

CONTACT_TYPE = (
    (u'Email Address',u'Email Address'),
    (u'Landline',u'Landline'),
    (u'Mobile Number',u'Mobile Number'),
    (u'Fax',u'Fax'),
)

class ContactInformation(models.Model):
    user = models.ForeignKey(User, verbose_name="User")
    value = models.CharField("Value", max_length=120)
    type = models.CharField("Type", max_length=50, choices=CONTACT_TYPE)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
