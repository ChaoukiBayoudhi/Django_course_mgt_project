from django.db import models
class Person(models.Model):
    name=models.CharField(max_length=50)
    familyName=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    birthdate=models.DateField()
    class Meta:
        #abstract model : it will not create a table in the database
        abstract=True
        ordering=['name','familyName']
    
#2nd method to define choices : using a models.TextChoices class
class TutorGrade(models.TextChoices):
    ASST='Assistant'
    ASSOC='Associate'
    PROF='Professor'
    EXPR='Expert'

class Tutor(Person):
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

class Course(models.Model):
    #id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    startDate=models.DateField(auto_now_add=True)
    nbLectures=models.PositiveSmallIntegerField()
    duration=models.DurationField()
    coefficient=models.FloatField()
    courseAvatar=models.ImageField(upload_to='images/course_avatars/',blank=True,null=True)
    #relationship between Course and Tutor (1-*)
    tutor=models.ForeignKey(Tutor,on_delete=models.SET_NULL,null=True,
                            related_name='courses')
    class Meta:
        db_table='courses'
        ordering=['name'] #order by name in ascending order
        #ordering=['-name'] #order by name in descending order
        #ordering=['startDate','duration','coefficient']



class Student(Person):
    cin=models.CharField(max_length=8,primary_key=True)
    #relationship between Student and Course (*-*) through Enrollement
    courses=models.ManyToManyField(Course,through='Enrollement',
                                   through_fields=('student','course'),
                                   related_name='students')
    class Meta:
        db_table="students"

class Profile(models.Model):
    linkedIn=models.URLField()
    github=models.URLField()
    photo=models.ImageField(upload_to="images/student_images/",null=True, blank=True)
    #relationship between Profile and Student (1-1)
    student=models.OneToOneField(Student,on_delete=models.CASCADE,primary_key=True,
                                 related_name='profile')
    class Meta:
        db_table="profiles"
        ordering=["linkedIn","github"]
class Location(models.Model):
    locationNumber=models.CharField(max_length=10)
    streetName=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zipCode=models.CharField(max_length=10)
    #relationship between Location and Course (*-*)
    #this line will create a table named locations_courses (The association table)
    #related_name : the name of the reverse relation from the related object back to this one
    courses=models.ManyToManyField(Course,db_table='courses_locations',
                                   related_name='locations')
    class Meta:
        db_table="locations"
        constraints=[models.UniqueConstraint(
            fields=["locationNumber","streetName","zipCode"],
            name="unique_location"
        )]
class Enrollement(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    registrationDate=models.DateField(auto_now_add=True)
    result=models.FloatField()
    class Meta:
        db_table="enrollements"
        constraints=[models.UniqueConstraint(
            fields=["student","course"],
            name="unique_enrollement_student_course"
        )]
        ordering=["registrationDate"]
