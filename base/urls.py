from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('adding/<str:id>/', views.adding, name='adding'),
    path('delete/<str:id>/', views.delete, name='drop'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('reading/<str:id>', views.reading, name='reading'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_comment/<str:id>', views.delete_comment, name='delete_comment'),
    path('add_travel/', views.add_travel, name='add_travel'),
    path('delete_travel/<str:id>', views.delete_travel, name='delete_travel'),  # Updated name
]