# API Root: http://127.0.0.1:8000/api

from django.shortcuts import render

### new imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # a list of HTTP status codes that are used to handle responses from api
from django.db import models
from django.db.models import CharField

from profiles_api import serializers

# Create your views here.

# application logic for the endpoint assigned to this view 

# define a url (endpoint), assign it to this view,
# django rest_framework calls the appropriate func 
# in the view for theHTTP request you make
class HelloApiView(APIView):
    """Test API View"""

    # set a serializer
    serializer_class = serializers.HelloSerializer


    # HTTP get request for our API
    # to retrieve a list of objects or a specific object

    # request: a part of rest_framework and has details of the request to the API
    # format: adds a format suffix to the end of url
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        # has to be a list or a dictionary to covert it to JASON
        return Response({'message':'Hello', 'an_apiview':an_apiview})

    # when we receive a post request to our hello api
    def post(self, request):
        """Create a hello message with our name"""

        # retrieve a serializer and pass in the data that was sent in the request
        serializer = self.serializer_class(data=request.data)

        # validate the serializer
        if serializer.is_valid():
            # retrieve the name field from a valied data
            name = serializer.validated_data.get('name')

            message = f'Hello, {name}'

            # return message a s a response
            return Response({"message": message})
        
        # if response is invalid
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
    # HTTP put is used to make a request and update an entire object
    def put(self, request, pk=None): # pk: primary key or id of an object we are updating
        """Handle updating an object"""
        return Response({"method": "PUT"})
    
    # only update the fileds provided in the request
    def patch(self, request, pk=None):
        """"Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response ({"method": 'DELETE'})




### CREATING A VIEWSET: http://127.0.0.1:8000/api/hello-viewset/

# "http_method": "GET": /api/hello-viewset/1/

from rest_framework import viewsets

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        # retrieve a serializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # retrieve the name field
            name = serializer.validated_data.get('name')
            # create a message
            message = f'Hello {name}!'

            return Response({'message': message})
        
        else: # if data is not valid
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # for retrieving a specific object in our viewset
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})




### CREATE A VIEWSET TO ACCESS UserProfileViewSet SERIALIZER THROUGH AN ENDPOINT

# User Profile List: GET /api/profile/
# User Profile Instance: GET /api/profile/<user id>/

from profiles_api import models

# ModelViewSet: designed for managing models through our api
# connect it to the serializer class and provide it 
# a query set so it knows which object it will manage through this viewset.

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    # assign a serializer class
    serializer_class = serializers.UserProfileSerializer
    
    # the viewset that we will manage through this model viewset
    queryset = models.UserProfile.objects.all()


    # Explanation: the Django rest framework knows the standard functions you'd want to perform on a viewsset (list, create, list, destroy..)
    # and takes cares of all these functions to manage specific model objects in a dataset 
    # by assigning a serializer_class to a model serializer and the quesryset