from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status # Handy HTTP status codes that we can use while returning responses from our api.

from profiles_api import serializers
# from django.shortcuts import render
#
# # Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
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

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        # self.serializer_class() - Standard way to retrieve the serializer class. Function that comes with the API view that retrieves the configured serializer class for view.

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def put(self,request,pk=None):
        """Handle updating an object"""
        # pk :- PUT to the URL with the id of the object we're updating. Taking the ID of the object to be updated.
        # PUT :- Complete update of the given object. Replacing the object.
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        # PATCH :- Partial update of the given object. Only update the fields given in the request.
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        # Deleting objects in the database
        return Response({'method': 'DELETE'})
