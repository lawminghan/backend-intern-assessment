from rest_framework import serializers
from django.contrib.auth import password_validation

from .models import WaveScanUser


class WaveScanUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WaveScanUser
        fields = ['id', 'email', 'password', 'role', 'firstName', 'lastName', 'company', 'designation']
        extra_kwargs = {
            'password' : {'write_only':True},
        }
    
    def create(self,validated_data):
        if validated_data['role'] == 'ADMIN':
            user = WaveScanUser.objects.create_superuser(**validated_data)
        else:
            user = WaveScanUser.objects.create_user(**validated_data)
        return user
      
    def update(self, instance, validated_data):
        #hash password
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        
        #updates the fields if they are present in validated_data
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        company = validated_data.get('company', instance.company)
        if company == "":
            company = None
        instance.company = company
        designation = validated_data.get('designation', instance.designation)
        if designation == "":
            designation = None
        instance.designation = designation
        instance.save()
        return instance

    def validate_password(self, value):
        password_validation.validate_password(password=value)
        return value

        
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaveScanUser
        fields = ['role']
