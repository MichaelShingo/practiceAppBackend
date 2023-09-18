from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if User.objects.filter(email=validated_data['email']).exists():
            raise ValueError
        user = User.objects.create_user(validated_data['email'], validated_data['password'], validated_data['first_name'], validated_data['last_name'])
        return user