from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status # Handy HTTP status codes that we can use while returning responses from our api.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
# from django.shortcuts import render
#
# # Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    # Add function to Http methods

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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    # Action performed on the API - list, create, retrieve, update, partial_update

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message' : 'Hello!', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create new hello message"""
        serializer  = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by it's ID"""
        return Response({'http_method': 'GET'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handling creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Set the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
