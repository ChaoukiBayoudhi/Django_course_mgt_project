from rest_framework import viewsets

from .serializers import TutorSerializer,StudentSerializer, CourseSerializer
from .models import Tutor, Student, Course
#impement CRUD (Create, Read/Retreive, Update, Delete ) on Tutor
#ModelViewSet has 6 predefined functions
#list() => to select all objects (  )
#retreive() =>get an object by id
#create() => insert new object
#update() => update complete object information by id
#partial_update() => to update partially an object by id
#destroy() => to remove an object by id
class TutorViewSet(viewsets.ModelViewSet):
    #CRUD  on all Tutors
    queryset=Tutor.objects.all()
    #or if we want to write CRUD only on Totors that have name starts with A
    #queryset=Tutor.objects.filter(name__startswith='A')
    serializer_class=TutorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
