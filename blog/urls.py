from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogPostList.as_view()),
    path('blog/', views.BlogPostView.as_view())
]