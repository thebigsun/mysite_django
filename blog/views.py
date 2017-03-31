from django.shortcuts import render, render_to_response

# Create your views here.
from blog.models import BlogsPost


def index(request):
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html',{'blog_list':blog_list})