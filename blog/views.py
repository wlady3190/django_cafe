from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
# Create your views here.


def blog (request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'list_blogs':blogs})

def category(request, categoryId):
    category = get_object_or_404(Category, id=categoryId)
    blogs = Blog.objects.filter(categories=category) #devulve los registro filtrados, 
    return render(request,'blog/category.html', {'list_blogs':blogs})

    
    