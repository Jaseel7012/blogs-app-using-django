from . import views
from django.urls import path
from django.contrib.auth import views as auth_view
urlpatterns=[
    path('register/',views.register,name='user-register'),
    path('profile/',views.profile,name='user-profile'),
    path('',auth_view.LoginView.as_view(template_name='user/login.html'),name='user-login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='user/logout.html'),name='user-logout'),
    





]