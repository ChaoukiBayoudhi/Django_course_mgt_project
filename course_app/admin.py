from django.contrib import admin
from .models import Course,Student,Tutor,Enrollement,Profile,Location
# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Enrollement)
admin.site.register(Profile)
admin.site.register(Location)