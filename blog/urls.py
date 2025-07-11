from django.urls import path

from rest_framework import routers

from . import views

urlpatterns = [
    path('', views.HomepageView.as_view()),
    path('posts/', views.BlogPostList.as_view()),
    path('posts/<int:pk>/', views.PostView.as_view())
]

router = routers.DefaultRouter()
router.register('api/posts', views.PostViewSet)

urlpatterns += router.urls