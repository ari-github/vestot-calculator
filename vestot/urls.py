from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_veset/', views.add_veset, name='add_veset'),
    path('delete_veset/<int:num>', views.delete_veset, name='delete_veset'),
]