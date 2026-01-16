from django.urls import path
from .views import IndexView, PostListView, PostDetailView

urlpatterns = [
    path('',  IndexView.as_view(), name='index'),
    path('posts/', PostListView.as_view()),
    path('post/<int:pk>', PostDetailView.as_view())
]