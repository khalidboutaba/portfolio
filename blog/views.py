from django.shortcuts import render,get_object_or_404
from .models import Blog

def blog(request):
    blogs=Blog.objects.order_by('-pub_date')[2:]
    latest_blogs=Blog.objects.order_by('-pub_date')[:2]
    print(blogs)
    return render(request,'blog/blog.html',{'blogs':blogs, 'latest_blogs':latest_blogs})

def detail(request, id):
    detailblog = get_object_or_404(Blog, pk=id)
    return render(request, 'blog/detail.html',{'detailblog':detailblog})