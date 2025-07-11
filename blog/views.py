from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Post

from rest_framework import viewsets
from .serializers import PostSerializer

import markdown
    
class HomepageView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/homepage.html')

class BlogPostList(ListView):
    model = Post
    template_name='blog/post_list.html'
    
    def get_queryset(self):
        return super().get_queryset().order_by('-id')

class PostView(DetailView):
    model = Post
    context_object_name = 'post'

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)