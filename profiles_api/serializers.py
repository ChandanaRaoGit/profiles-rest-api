from rest_framework import serializers

# Serializer is a feature from the django rest framework that allow us to easily confer data input into python object and vice-versa.
# To receive the output that comes from POST or UPDATE method. Takes care of validation rules also.

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)
