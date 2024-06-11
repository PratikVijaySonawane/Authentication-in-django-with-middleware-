from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view,name='register'),
    path('login/', login_view,name='login'),
    path('logout/', logout_view,name='logout'),
    path('dashboard/', dashboard_view,name='dashboard'),
]
