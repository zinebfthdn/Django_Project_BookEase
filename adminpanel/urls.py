from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='admin_index'),
    path('approve/<int:book_id>/', views.approve_book, name='approve_book'),
    path('edit/<int:book_id>/', views.edit_book, name='admin_edit_book'),
    path('view/<int:book_id>/', views.view_book, name='view_book'),
    path('download/<int:book_id>/', views.download_book, name='admin_download_book'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit_publisher/<int:publisher_id>/', views.edit_publisher, name='edit_publisher'),
]
