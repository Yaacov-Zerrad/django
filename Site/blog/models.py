from django.db import models
from django.urls import reverse

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField()
    activate = models.BooleanField(default=True)
    
    
    class Meta:
        """for plur and sing in admin"""
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")
        
        
    def __str__(self) :
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"pk": self.pk})
        