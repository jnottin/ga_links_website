from django.db import models

# Create your models here.
class GaLesson(models.Model):
    lesson_name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    type_of_lesson = models.CharField(max_length=200)
    lesson_url = models.TextField()
    date = models.CharField(max_length=50)
    
    def __str__(self):
        return self.lesson_name