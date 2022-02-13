from rest_framework.views import APIView
from rest_framework.views import Response
# from django.shortcuts import render
#
# # Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        # request contains the details of the request being made to the api.
        """Returns a list of APIView features"""
        an_apiview  = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over the application logic',
            'Is mapped manually to URL'
        ]

        return Response({'message':"Hello!",'an_apiview':an_apiview})
