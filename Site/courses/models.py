from django.db import models
from django.urls import reverse

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField()
    activate = models.BooleanField(default=True)
    
    
    class Meta:
        """for plur and sing in admin"""
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")
        
        
    def __str__(self) :
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"pk": self.pk})
        
