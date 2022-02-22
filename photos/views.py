from django.shortcuts import redirect, render
from .models import Category, Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PhotoForm
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage

def gallery(request):
  category = request.GET.get('category')
  if category == None:
    photos = Photo.objects.all()
  else:
    photos = Photo.objects.filter(category__name__contains=category)
  categories = Category.objects.all()

  page = request.GET.get('page', 1)
  paginator = Paginator(photos, 3) 
  try:
    photos = paginator.page(page)
  except PageNotAnInteger:
    photos = paginator.page(1)
  except EmptyPage:
    photos = paginator.page(paginator.num_pages)
 
  context = {'categories':categories, 'photos':photos}
  return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
  photo = Photo.objects.get(id=pk)
  context = {'photo':photo}
  return render(request, 'photos/photo.html', context)

def addPhoto(request):
  categories = Category.objects.all()
  if request.method == 'POST':
    data = request.POST
    images = request.FILES.getlist('images')
    
    if data['category'] != 'none':
      category = Category.objects.get(id=data['category'])
    elif data['category_new'] != '':
      category, created = Category.objects.get_or_create(name=data['category_new'])
    else:
      category = None
      
    for image in images:
      photo = Photo.objects.create(
        category=category,
        description=data['description'],
        image=image,
      )
    return redirect('/')
  context = {'categories':categories}
  return render(request, 'photos/add.html', context)

