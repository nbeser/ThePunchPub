from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages_index, name='pages_index'),
    path('user/<username>', views.user_index, name='user_index'),
    path('menu/', views.pages_menu, name='pages_menu'),
    path('slide/add', views.create_slider, name='create_slider'),
    path('slide/edit/<id>', views.edit_slider, name='edit_slider'),
    path('slide/delete/<id>', views.delete_slider, name='delete_slider'),
    path('menu/<slug:slug>', views.products_by_category, name='products_by_category'),
]