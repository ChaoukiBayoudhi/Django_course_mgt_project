from rest_framework.routers import DefaultRouter
from .views import TutorViewSet,StudentViewSet,CourseViewSet
router=DefaultRouter()
#by registering a ViewSet we add 2 paths with 6 possibilities
#http://127.0.0.1:8000/course-app/tutors/ via GET Http method (get all tutors)
#http://127.0.0.1:8000/course-app/tutors/ via POST Http method (add a new tutor)
#http://127.0.0.1:8000/course-app/tutors/5 via GET Http method (get the tutor having the id = 5)
#http://127.0.0.1:8000/course-app/tutors/5 via PUT Http method (update the complete Tutor fields)
#http://127.0.0.1:8000/course-app/tutors/5 via PATCH Http method (update some of Tutor fields)
#http://127.0.0.1:8000/course-app/tutors/5 via DELETE Http method (remove the tutor having the id = 5)
router.register(r'tutors',TutorViewSet)
router.register(r'students',StudentViewSet)
router.register(r'courses',CourseViewSet)
urlpatterns = router.urls