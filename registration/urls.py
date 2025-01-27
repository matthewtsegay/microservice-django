from django.urls import path
from . import views

urlpatterns = [
    path('register/<int:course_id>/', views.register_for_course, name='register_for_course'),
]
