from django.urls import path, include

from . import views


app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name="register"),
    path('user_profile/', views.user_profile, name="user_profile"),
   
]