from django.db import models
from PIL import Image

class Category(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  
  def __str__(self):
    return self.name
  
class Photo(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
  image = models.ImageField(null=False, blank=False)
  description = models.TextField()
  
  def __str__(self):
    return self.description
    
