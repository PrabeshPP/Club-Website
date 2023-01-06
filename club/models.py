from django.db import models
import uuid
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _



# Create your models here.
class CustomUserManager(BaseUserManager):
    use_in_migrations=True

    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email can not be empty!")
        else:
            email=self.normalize_email(email)
            user=self.model(email=email,**extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(email,password,**extra_fields)
        

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(_('email'),unique=True,default='')
    name=models.CharField(_('name'),max_length=120,blank=False)
    is_superadmin=models.BooleanField(_('is_superadmin'),default=False)
    is_active=models.BooleanField(_('is_active'),default=True)
    is_staff=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    objects=CustomUserManager()


    class Meta:
        verbose_name=_('User')
        verbose_name_plural=_('Users')
    
    def __str__(self) -> str:
        return self.email





class TimeStampsModel(models.Model):
    created_at=models.TimeField(auto_now_add=True)
    updated_at=models.TimeField(auto_now=True)
    
    class Meta:
        abstract=True

class Executives(TimeStampsModel):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name=models.CharField(max_length=120)
    role=models.CharField(max_length=120)
    image=models.FileField(upload_to="executives/",default=None,max_length=250,null=False)
    description=models.TextField()

    def __str__(self) -> str:
        return self.name


class Resources(TimeStampsModel):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    title=models.CharField(max_length=120)
    description=models.TextField()
    resourceURL=models.TextField()
    image=models.FileField(upload_to="resources/",default=None,max_length=250,null=False)

