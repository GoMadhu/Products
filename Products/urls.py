from django.urls import path

from .views import home, update, deleteproduct, delete_products

urlpatterns = [
    path('', home, name="home"),
    path('update/<int:id>', update, name="update"),
    path('deleteproduct/<int:id>', deleteproduct, name="deleteproduct"),
    path('delete_products', delete_products, name="delete_products"),
]