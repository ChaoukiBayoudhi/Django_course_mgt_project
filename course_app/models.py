from django.db import models

class Course(models.Model):
    #id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    startDate=models.DateField(auto_now_add=True)
    nbLectures=models.PositiveSmallIntegerField()
    duration=models.DurationField()
    coefficient=models.FloatField()
    courseAvatar=models.ImageField(upload_to='images/course_avatars/',blank=True,null=True)
    class Meta:
        db_table='courses'
        ordering=['name'] #order by name in ascending order
        #ordering=['-name'] #order by name in descending order
        #ordering=['startDate','duration','coefficient']

#2nd method to define choices : using a models.TextChoices class
class TutorGrade(models.TextChoices):
    ASST='Assistant'
    ASSOC='Associate'
    PROF='Professor'
    EXPR='Expert'

class Tutor(models.Model):
    name=models.CharField(max_length=50)
    familyName=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    birthdate=models.DateField()
    photo=models.ImageField(upload_to='images/tutor_avatars/',blank=True,null=True)
    #1st method to define choices : using a list of tuples
    '''grade=models.CharField(max_length=50,choices=[('ASST','Assistant'),
                                                  ('ASSOC','Associate'),
                                                  ('PROF','Professor'),
                                                  ('EXPR','Expert')],
                                                  default='ASST')
                                                  
    '''
    #2nd method to define choices : using a models.TextChoices class
    grade=models.CharField(max_length=50,choices=TutorGrade.choices,default=TutorGrade.ASST)
    class Meta:
        db_table='tutors'
        ordering=['name','familyName']


class Student(models.Model):
    cin=models.CharField(max_length=8,primary_key=True)
    name=models.CharField(max_length=100)
    familyName=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    birthDate=models.DateField()
    class Meta:
        db_table="students"
        ordering=["name","familyName"] #sort by name in ascending order, then by familyName in ascending order

class Profile(models.Model):
    linkedIn=models.URLField()
    github=models.URLField()
    photo=models.ImageField(upload_to="images/student_images/",null=True, blank=True)
     class Meta:
        db_table="profiles"
        ordering=["linkedIn","github"]
class Location(models.Model):
    locationNumber=models.CharField(max_length=10)
    streetName=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zipCode=models.CharField(max_length=10)

    class Meta:
        db_table="locations"
        constraints=[models.UniqueConstraint(
            fields=["locationNumber","streetName","zipCode"],
            name="unique_location"
        )]
#
