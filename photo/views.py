from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/detail.html', {'photo':photo})

def post(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'photo/post.html', {'form':form})

def edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/post.html', {'form':form})