from django.urls import path
from . import views



urlpatterns = [
    path('', views.notifications_home, name='notifications_home'),
    path('profile/', views.profile_view, name='profile'),
    path('send/', views.send_notifications, name='send_notifications'),
    path('view/', views.view_notifications, name='view_notifications'),
]
