from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('photo/<int:pk>/', views.detail, name='detail'),
    path('photo/new/', views.post, name='post'),
    path('photo/<int:pk>/edit/', views.edit, name='edit'),
]