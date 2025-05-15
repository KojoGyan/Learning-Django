from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello, name = 'hello'),
    path("hello/<str:name>/", views.greetings, name = 'greetings'),
    path("birthday_v1", views.birthday_v1, name = "birthdays_v1"),
    path("birthday_v2", views.birthday_v2, name = "birthday_v2")
]
