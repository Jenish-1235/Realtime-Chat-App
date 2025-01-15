from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    # We might have separate signup, login, logout, etc.:
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('get_old_messages/<str:username>/', views.get_old_messages, name='get_old_messages'),

]
