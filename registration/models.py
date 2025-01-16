from django.db import models # type: ignore
from django.db import models # type: ignore
from users.models import User
from course_catalog.models import Course

class Registration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} registered for {self.course.name}'

# Create your models here.
