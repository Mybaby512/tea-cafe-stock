from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('add/', views.equipment_create, name='equipment_create'),
    path('edit/<int:pk>/', views.equipment_update, name='equipment_update'),
    path('delete/<int:pk>/', views.equipment_delete, name='equipment_delete'),
]