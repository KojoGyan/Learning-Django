from django.urls import path
from . import views 

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello/<str:name>/', views.greetings, name='greetings'),
]