from django.urls import path
from .views import  result, checkResponseSheet
from django.contrib.auth import views as auth_views


app_name = 'result'
urlpatterns = [
    path('', result, name='result'),
    path('check-response-sheet/<int:exam_id>', checkResponseSheet, name='check-response-sheet'),

]
