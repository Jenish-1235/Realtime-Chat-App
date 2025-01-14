from django.urls import path
from .views import signup_view, chat_home, chat_room

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('', chat_home, name='chat_home'),
    path('<str:username>/', chat_room, name='chat_room'),
]
