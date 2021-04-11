from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_home, name='calendar-home'),
    path('<int:year>/<int:month>', views.month, name='calendar-month'),
]