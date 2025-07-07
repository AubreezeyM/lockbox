from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomepageView.as_view()),
    path('posts/', views.BlogPostList.as_view()),
    path('posts/<int:pk>/', views.MarkdownView.as_view())
]