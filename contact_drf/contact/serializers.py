from rest_framework import serializers
from contact.models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['id','name','email','phone','created_at']
    

    def validate_phone(self, value):
        phone_str = str(value)

        if len(phone_str) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        
        if not phone_str.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")

        if phone_str[0] not in ['6', '7', '8', '9']:
            raise serializers.ValidationError("Phone number must start with 6, 7, 8, or 9.")

        return value