from django.db import models
# additional imports
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    # set password=None if no password provided
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        # make email address ...
        email = self.mormalize_email(email)
        # creating user model
        user = self.model(email=email, name=name)

        # set_password() converts password to a hash (encrypted)
        user.set_password(password)
        # Save a usermodel 
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with iven details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True # was automatically created by PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=225, unique=True) # email has to be unique
    name = models.CharField(max_length=225)

    # Permission System

    # determines if user's profile is activated or not.
    # By default, every user's profile is activated
    is_active = models.BooleanField(default=True)

    # checks if a user is a part of staff
    is_staff = models.BooleanField(default=False)

    # manager class
    objects = UserProfileManager()

    # overwriting a username to email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # retrieving user's full name
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    # retrieving user's full name
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    # convert email to a string
    def __str__(self):
        """Return string representation of our user"""
        return self.email
    


