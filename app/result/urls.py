from django.urls import path
from .views import  result
from django.contrib.auth import views as auth_views


app_name = 'result'
urlpatterns = [
    path('', result, name='result'),

]
