from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.loginForm, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('emp_details/', views.employeeDetails, name='emp_details'),
    path('emp_detail_/', views.employeeForm, name='emp'),
]