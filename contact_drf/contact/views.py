from django.shortcuts import render
from contact.models import *
from contact.serializers import ContactSerializer
from rest_framework import viewsets
# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all().order_by('-created_at')
    serializer_class=ContactSerializer