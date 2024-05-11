from django.shortcuts import render
from django.views.generic import DetailView
from blog.models import Post, Category, Tag



class PostView(DetailView):
    model = Post
    template_name = "post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    
