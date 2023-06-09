from django.shortcuts import render

### new imports
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# application logic for the endpoint assigned to this view 

# define a url (endpoint), assign it to this view,
# django rest_framework calls the appropriate func 
# in the view for theHTTP request you make
class HelloApiView(APIView):
    """Test API View"""

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