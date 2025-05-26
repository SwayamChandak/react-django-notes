from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, NoteSerializer
from .models import Note
# Create your views here.

class CreateUserView(generics.CreateAPIView): #generics is inbuilt view that will handle creating object for us
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer): #override the default create function to check validity of input
        if serializer.is_valid(): #check if title length is less than 100 or not etc 
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)            