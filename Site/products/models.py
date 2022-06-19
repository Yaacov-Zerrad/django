from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.urls import reverse

class Products(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    image = models.ImageField(upload_to='images',blank=True)
    slug = models.SlugField(null=True)
    activate = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")
        
    def __str__(self) :
        return self.name
    
    def get_absolute_url(self):
        return reverse("update", kwargs={"pk": self.pk})
    
    
    
