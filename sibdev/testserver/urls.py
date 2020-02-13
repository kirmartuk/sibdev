from django.urls import path
from .views import *
app_name = "test"

urlpatterns = [
    path('get', get),
    path('post', post),
    ]
