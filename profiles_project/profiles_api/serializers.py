# A serializer is a feature from a Django rest framework that
# allows to covert data inputs into Python objects and vice versa.
# similar to Django forms

from django.db import models
from django.db.models import CharField
from rest_framework import serializers

# Create a serializer to receive content that we post to the API
class HelloSerializer(serializers.Serializer): # Serializer is a classname. Thant's why it's in capital
    """Serializers a name field for testing our APIView"""

    # specify fields that you want to accept in your serializer input
    # serializer is going to validate your input by rules

    name = serializers.CharField(max_length=10)