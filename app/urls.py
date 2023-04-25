from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="All Chats"),
    path('friend/<str:pk>', views.friend_detail, name="friend_detail"),
    path('sent_msg/<str:pk>', views.sentMessage, name="sent_msg")
]
