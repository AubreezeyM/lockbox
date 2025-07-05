from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post

class BlogPostView(View):

    def get(self, request):
        return render(request, 'base.html')
    
class BlogPostList(View):
    posts_qs = Post.objects.all().order_by('-id')
    all_posts = {'posts': posts_qs}

    def get(self, request):
        return render(request, 'homepage.html', self.all_posts)
