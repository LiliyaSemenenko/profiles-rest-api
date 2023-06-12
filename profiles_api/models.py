from django.db import models
# additional imports
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# use to retrieve settings from settings.py file in project folder
# in particular, we'' retrieve AUTH_USER_MODEL
from django.conf import settings

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    # set password=None if no password provided
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        # make email address ...
        email = self.normalize_email(email)
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
    

### CREATE PROFILE FEED API ###

# Model that allows users to store status updates in the system 
# so every time they create a new update it's going to create 
# a new profile feed item object and associate that object with
# the user that created it.
class ProfileFeedItem(models.Model):
    """Profile status update"""

    # Use a foreign key field it sets up a foreign key relationship 
    # in the database to a remote model.
    # The benefit is that it allows you to ensure that the integrity
    # of the database is maintained so you can never create a 
    # profile feed item for a user profile that doesn't exist.
    user_profile = models.ForeignKey(
        # name of the remote model of this foreign key
        # retrieve it from AUTH_USER_MODEL in setting.py
        settings.AUTH_USER_MODEL,
        
        # if the remote field (user profile) is deleted, 
        # cascade the changes down through all the deleted feed
        # so remove all the feed items associated with the user profile
        # Note: on_delete = models.setnull will not delete the feed items, just the profile
        on_delete = models.CASCADE
    )
    # containes text of the field update
    status_text = models.CharField(max_length=225)

    # once we create a new feed item automatically add the date time stamp that the item was created
    created_on = models.DateTimeField(auto_now_add=True)

    # string represenattion of our model (converting model instance to a string)
    def __str__(self):
        """Return the model as a string"""
        return self.status_text