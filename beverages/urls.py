from django.urls import path
from . import views

urlpatterns = [
    path('', views.beverages_index, name='beverages_index'),
    path('create-beverages', views.create_beverages, name='create_beverages'),
    path('delete-beverages/<slug>', views.delete_beverages, name='delete_beverages'),
    path('edit-beverage/<slug>', views.edit_beverages, name='edit_beverages'),
    path('create-beverage-category', views.create_beverageCategories, name='create_beverageCategories'),
    path('edit-beverage-category/<slug>', views.edit_beverageCategories, name='edit_beverageCategories'),
    path('delete-beverage-category/<slug>', views.delete_beverageCategories, name='delete_beverageCategories'),
    path('<category>', views.beverages_index, name='beveragesByCategory'),
]