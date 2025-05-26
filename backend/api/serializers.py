from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

#django uses ORM, object relational mapping. serializers convert the object to json format to forwad it to frontend 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User #inbuilt django model
        fields=["id", "username", "password"]
        extra_kwargs={"password": {"write_only":True}}

    def create(self, validated_date):
        user=User.objects.create_user(**validated_date)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=["id", "title", "content", "created_at", "author"]    
        extra_kwargs={"author": {"read_only": True}}