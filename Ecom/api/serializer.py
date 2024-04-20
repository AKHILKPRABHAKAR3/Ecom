from rest_framework import serializers
from store.models import User,Product

class Signup(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','email']
        read_only_fields=['id']
class Login(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class productserializer(serializers.ModelSerializer):
    class Meta:

        model=Product
        fields="__all__"