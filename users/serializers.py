from dataclasses import field
from wsgiref.validate import validator
from rest_framework import serializers,validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    
    
    #*validators for fields
    email = serializers.EmailField(
        required = True,
        validators =[validators.UniqueValidator(queryset=User.objects.all())]
    )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        #* to avoid explicit password
        style = {'input_type':'password'}
    )
    
    #* No need for validations we will check both are same or not
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {'input_type':'password'}
        
    )
    
    #* no password2 as default we will create custom func
    class Meta:
        model = User
        fields = ['username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'
        ]
        #* arbitrary additional keyword arguments
        extra_kwargs ={
            'password':{'write_only':True},
            'password2':{'write_only':True},
        }
        
    #* overwriten for password2    
    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data.pop('password2')
        user= User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
    #* serializers validations => object level || field level
    def validate(self,data):
        
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords must match')
        return data