from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.BlogPostList.as_view()),
    path('<int:pk>/', views.MarkdownView.as_view())
]