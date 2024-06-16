from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.saytext, name='saytext'),
    path('hellohtt/', views.say_hello, name='say_hello'),
]