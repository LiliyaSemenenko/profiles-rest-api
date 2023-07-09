# A serializer is a feature from a Django rest framework that
# allows to covert data inputs into Python objects and vice versa.
# similar to Django forms

# In Django, a serializer is a component that converts complex data types, such as Django models, 
# into a format that can be easily rendered into various output formats, such as JSON, XML, or HTML.

# In summary, serializers.Serializer is a flexible and customizable base class for defining serializers, 
# while serializers.ModelSerializer provides higher-level abstraction and automates much of the serialization/deserialization process 
# by leveraging the model's fields and relationships.

# Note: Django REST Framework (DRF)

from django.db import models
from django.db.models import CharField
from rest_framework import serializers

# Create a serializer to receive content that we post to the API
class HelloSerializer(serializers.Serializer): # Serializer is a classname. Thant's why it's in capital
    """Serializers a name field for testing our APIView"""

    # specify fields that you want to accept in your serializer input
    # serializer is going to validate your input by rules

    name = serializers.CharField(max_length=10)


### CREATING PROFILES API ###

from profiles_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    # to configure a serializer to point at a specific model in our project
    class Meta:
        model = models.UserProfile
        # list of fields to make accessible in our API/model
        fields = ('id', 'email', 'name', 'password')
        
        extra_kwargs = {
            'password': {
                'write_only': True, # you can only use it to update/create new objects, but NOT to retrieve
                'style': {'input_type': 'password'} # input_type: password: means you can't see letters, just dots
            }
        }

    # create a new user
    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile.objects.create_user(
            # retreive email from validated data
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        # return a new user
        return user
    

    # The default update logic for the Django REST Framework (DRF) ModelSerializer code 
    # will take whatever fields are provided (in our case: email, name, password) 
    # and pass them directly to the model.

    # This is fine for the email and name fields, 
    # however the password field requires some additional logic 
    # to hash the password before saving the update.

    # Therefore, we override the Django REST Framework's update() method 
    # to add this logic to check for the presence password 
    # in the validated_data which is passed from DRF when updating an object.

    # check for the presence password in the validated_data 
    # which is passed from DRF when updating an object.
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            # pop(): assign the value and remove from the dictionary
            password = validated_data.pop('password') 
            # set_password(): saves the password as a hash
            instance.set_password(password)

        # super().update(): to pass the values to the existing 
        # DRF update() method, to handle updating the remaining fields.
        return super().update(instance, validated_data)
    


### CREATING PROFILE FEED API ###

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        
        # id and created_on is set up by default and is set to READ ONLY
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        
        # user_profile has to be set when the user is authentificated
        # therefore, user_profile has to be made READ ONLY as well
        extra_kwargs = {'user_profile': {'read_only': True}}
