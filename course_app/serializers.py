from rest_framework import serializers
from .models import Person, Tutor, Student,Course,Enrollement
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        #fields=['id','name','familyName']
        fields='__all__'
class TutorSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        model=Tutor

class StudentSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        model=Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class EnrollementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enrollement
        fields='__all__'