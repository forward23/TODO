from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('<int:pk>/password/', views.PasswordUpdateView.as_view(), name='password'),

]