from django.urls import path
from . import views

urlpatterns = [
    path('', views.tea_list, name='tea_list'),
    path('add/', views.tea_add, name='tea_add'),
    path('edit/<int:pk>/', views.tea_edit, name='tea_edit'),
    path('delete/<int:pk>/', views.tea_delete, name='tea_delete'),
]