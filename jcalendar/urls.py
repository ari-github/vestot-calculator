from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_home_view, name='calendar-home'),
    path('<int:year>/<int:month>', views.month_view, name='calendar-month'),
]