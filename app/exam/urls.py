from django.urls import path
from .views import instructions, question, section, all_questions
from django.contrib.auth import views as auth_views


app_name = 'exam'
urlpatterns = [
    path('instructions/', instructions, name='instructions'),
    path('question/<int:pk>/', question, name='question'),
    path('question/all', all_questions, name='all-question'),
    path('section/', section, name='section'),
    
]
