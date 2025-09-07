from django.contrib import admin
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("products/", views.product_list, name="product_list"),
    path("products/<slug:slug>/", views.product_detail, name="product_detail"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
