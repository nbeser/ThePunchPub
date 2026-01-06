from django.urls import path
from . import views

urlpatterns = [
    path('', views.brunch_index, name='brunch_index'),
    path('create-brunch', views.create_brunch, name='create_brunch'),
    path('delete-brunch/<slug>', views.delete_brunch, name='delete_brunch'),
    path('edit-brunch/<slug>', views.edit_brunch, name='edit_brunch'),
    path('create-brunch-category', views.create_brunchCategories, name='create_brunchCategories'),
    path('edit-brunch-category/<slug>', views.edit_brunchCategories, name='edit_brunchCategories'),
    path('delete-brunch-category/<slug>', views.delete_brunchCategories, name='delete_brunchCategories'),
]