from django.urls import path
from .views import instructions, question, section
from django.contrib.auth import views as auth_views


app_name = 'exam'
urlpatterns = [
    path('instructions/', instructions, name='instructions'),
    path('question/', question, name='question'),
    path('section/', section, name='section'),
    
]
