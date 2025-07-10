from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Post

import markdown
    
class HomepageView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/homepage.html')

class BlogPostList(ListView):
    model = Post
    template_name='blog/post_list.html'
    
    def get_queryset(self):
        return super().get_queryset().order_by('-id')

class MarkdownView(DetailView):
    model = Post
    
    def get(self, request, *args, **kwargs):
        md = markdown.Markdown(extensions=['fenced_code'])

        # quick conversion to markdown for the view
        this_post = self.model.objects.get(pk=kwargs['pk'])
        this_post.content = md.convert(this_post.content)

        return render(request, 'blog/markdown_view.html', {'post': this_post})

