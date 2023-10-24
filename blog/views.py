from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from category.models import Category
from django.contrib import messages
from .forms import Content

# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog.html",{'blogs' : blog})

def createBlog(request):
    instance = Blog(author=request.user.username)
    form = Content(instance=instance)
    return render(request, "addblog.html" , {'forms' : form})

def storeBlog(request):
    title = request.POST.get('title')
    deskripsi = request.POST.get('deskripsi')
    categor = request.POST.get('categoryName')
    category_instance = Category.objects.get(categoryName=categor)
    author = request.user.username
    Blog.objects.create(title=title,deskripsi=deskripsi,categoryName=category_instance,author=author)
    return redirect('blog')

def editBlog(request , id):
    blog = get_object_or_404(Blog , id = id)
    form = Content(instance = blog)
    return render(request , "editBlog.html", {'forms' : form , 'blog' : blog})

def updateBlog(request,id):
    blog = get_object_or_404(Blog, id = id)
    form = Content(request.POST , instance= blog)
    form.save()
    return redirect("blog")

def deleteBlog(request,id):
    blog = get_object_or_404(Blog, id = id)
    blog.delete()

    return redirect('blog')
      