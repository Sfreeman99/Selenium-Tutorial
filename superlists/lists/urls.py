from django.urls import path, include
from lists import views

app_name = 'lists'

urlpatterns = [path(
    '/',
    views.home_page,
    name='home', )]
