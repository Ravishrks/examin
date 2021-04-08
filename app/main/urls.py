from django.urls import path
from . import views as main_view

app_name = 'main'
urlpatterns = [
    path('', main_view.index, name='index'),

    # path('robots.txt/', main_view.robots, name='robots'),


]
