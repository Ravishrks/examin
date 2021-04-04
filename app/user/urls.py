from django.urls import path
from . import views as user_view
from user.views import  Register, terms, cookie_policy, data_policy
from django.contrib.auth import views as auth_views


app_name = 'user'
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]
