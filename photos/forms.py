from django.forms import ModelForm
from .models import Photo, Category

class PhotoForm(ModelForm):
  class Meta:
    model = Photo
    fields = '__all__'

