from django.shortcuts import render
from django.views import View
from .models import BlogPost


class IndexView(View):
    def get(self, request):
        blog_posts = BlogPost.objects.all()
        return render(request, "blog/index.html", {"blog_posts": blog_posts})


class DetailView(View):
    def get(self, request, pk):
        blog_post = BlogPost.objects.get(pk=pk)
        return render(request, "blog/detail.html", {"blog_post": blog_post})
