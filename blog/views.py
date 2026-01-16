from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Post

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post

class PostListView(ListView):
    model = Post
    queryset = Post.objects.order_by('-post_id')