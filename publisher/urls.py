from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='publisher_index'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('download/<int:book_id>/', views.download_book, name='download_book'),
]
