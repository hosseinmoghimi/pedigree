from rest_framework import serializers
from .models import *
class PersonSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=['id','first_name','get_admin_url','last_name','image','birthdate','get_absolute_url','full_name','deathdate']

  


class FamilySerializer(serializers.ModelSerializer):
    father=PersonSerializer1()
    mother=PersonSerializer1()
    childs=PersonSerializer1(many=True)
    class Meta:
        model=Person
        fields=['id','father','mother','childs']
class PersonSerializer(serializers.ModelSerializer):
    family_fathers=FamilySerializer(many=True)
    family_mothers=FamilySerializer(many=True)
    family_childs=FamilySerializer(many=True)
    class Meta:
        model=Person
        fields=['id','first_name','family_fathers','family_mothers','family_childs','get_admin_url','last_name','image','birthdate','get_absolute_url','full_name','deathdate']

  