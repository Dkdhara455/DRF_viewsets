from rest_framework import serializers
from contact.models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['id','name','email','phone','created_at']
        