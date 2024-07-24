from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
    path('image/create/', views.image_create, name='image_create'),
    path('image/<int:pk>/update/', views.image_update, name='image_update'),
    path('image/<int:pk>/delete/', views.image_delete, name='image_delete'),
]
