from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("new_item/", views.new_item, name="new-item"),
    path("edit_item/<int:pk>/", views.edit_item, name="edit-item"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path('delete/<int:pk>/', views.delete_view, name="delete"),
    path('search/', views.search, name='search'),
    path('properties/', views.properties_list, name='properties_list'),
    path('properties/<int:id>/', views.properties_detail, name='properties_detail'),
    path('properties/<int:id>/buy/', views.buy_property, name='buy_property'),
    path('properties/<int:id>/confirm_purchase/', views.confirm_purchase, name='confirm_purchase'),
]
