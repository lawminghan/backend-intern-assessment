from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class WaveScanUserManager(BaseUserManager):
    def create_user(self, email, role, firstName, lastName, password=None, **kwargs):
        """
        Creates and saves a User with the given email, role, firstName, lastName and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not role:
            raise ValueError('Users must have a role')
        if not firstName:
            raise ValueError('Users must have a First Name')
        if not lastName:
            raise ValueError('Users must have a Last Name')
        
        user = self.model(
            email=self.normalize_email(email),
            role = role,
            firstName = firstName,
            lastName = lastName,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, role, firstName, lastName, password=None, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
                        role = role,
            firstName = firstName,
            lastName = lastName,
            **kwargs
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



# Create your models here.
class WaveScanUser(AbstractBaseUser):

    class RoleInCompany(models.TextChoices):
        ADMIN = "ADMIN"
        MEMBER = "MEMBER"
        TECHNICIAN = "TECHNICIAN"
    
    # id field is present in AbstractBaseUser
    # password field is present in AbstractBaseUser
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True, 
                              null=False
                              )
    role = models.CharField(max_length=30, 
                            null=False, 
                            choices = RoleInCompany.choices
                            )
    firstName = models.CharField(max_length=30, 
                                 null=False
                                 )
    lastName = models.CharField(max_length=30, 
                                null=False
                                )
    company = models.CharField(max_length=100, 
                               null=True,
                               blank=True
                               )
    designation = models.CharField(max_length=50, 
                                   null=True,
                                   blank=True
                                   )
    
    def __str__(self):
        return self.email
    
    #Fields required to use Django Admin 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'firstName', 'lastName']
    objects = WaveScanUserManager()
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    # Override save to update self.is_admin when self.role changes
    def save(self, *args, **kwargs):
        if self.role == self.RoleInCompany.ADMIN:
            self.is_admin = True
        else:
            self.is_admin = False
        super().save(*args, **kwargs)
    
    
    
