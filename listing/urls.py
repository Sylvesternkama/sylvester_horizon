from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('create/', views.create_listing, name='create_listing'),
    path('', views.view_listings, name='view_listings'),
    path('<int:listing_id>/', views.view_listing_detail, name='view_listing_detail'),
    path('advertisements/', views.advertisements, name='advertisements'),
]