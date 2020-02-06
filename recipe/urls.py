from django.contrib import admin
from django.urls import path 
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeletelView, UserPostListView, PostSearchList, IngreUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='recipe-home'),
    path('about/', views.about, name='recipe-about'),
    path('recipe/<int:pk>/', PostDetailView.as_view(),name='recipe-detail'),
    path('recipe/new/', PostCreateView.as_view(), name='recipe-new'),
	path('recipe/new/', IngreUpdateView.as_view(), name='ingred-update'),
    path('recipe/<int:pk>/update/', PostUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', PostDeletelView.as_view(), name='recipe-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('search/', PostSearchList.as_view(), name="recipe-search")
]
