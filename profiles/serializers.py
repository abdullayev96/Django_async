from rest_framework import serializers
from .models import UserProfile
from account.models import User
from adrf.serializers import ModelSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "Profiles"
        model = UserProfile
        fields = ('full_name', 'number', 'balance')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance

