from rest_framework import serializers 
from .models import Person 

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person 
        fields=['id','username','email','password','created_at','updated_at'] 