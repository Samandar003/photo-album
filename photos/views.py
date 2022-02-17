from django.shortcuts import redirect, render
from .models import Category, Photo
from .forms import PhotoForm
from django.contrib import messages

def gallery(request):
  categories = Category.objects.all()
  photos = Photo.objects.all()
  
  context = {'categories':categories, 'photos':photos}
  return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
  photo = Photo.objects.get(id=pk)
  context = {'photo':photo}
  return render(request, 'photos/photo.html', context)

def addPhoto(request):
  form = PhotoForm()
  if request.method == 'POST':
    form = PhotoForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'You uploaded picture')
      return redirect('/')
  
  context = {'form':form}
  return render(request, 'photos/add.html', context)

