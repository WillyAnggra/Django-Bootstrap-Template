from django.shortcuts import render, redirect, get_object_or_404
from category.models import Category
from .forms import createCategory

def kategori(request):
    kategori = Category.objects.all()
    return render(request, 'kategori.html', {'category' : kategori})

def create(request):
    form = createCategory()
    return render(request, 'addKategori.html', {'form' : form})

def store(request):
    Category.objects.create(categoryName = request.POST.get('categoryName'))
    return redirect('kategori')

def deleteKategori(request,id):
    kategori = get_object_or_404(Category, id = id)
    kategori.delete()
    return redirect('kategori')

def editKategori(request,id):
    kategori = get_object_or_404(Category, id = id)
    form = createCategory(instance=kategori)
    return render(request, 'editkategori.html', {'form' : form , 'kategori' : kategori})

def updateKategori(request,id):
    kategori = get_object_or_404(Category, id = id)
    form = createCategory(request.POST , instance= kategori)
    form.save()
    return redirect("kategori")