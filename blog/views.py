from django.shortcuts import render
from .models import Blog


# Create your views here.
def blog(request):
    blog_posts = Blog.objects.all()
    context = {'posts': blog_posts, }
    return render(request, "blogTemplates/blog.html", context)
