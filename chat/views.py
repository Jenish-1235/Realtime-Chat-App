from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat_home')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

def login_view(request):
    # You can use Django's built-in auth views with a template-based approach
    # For brevity, let's assume we have a custom form or we redirect to `django.contrib.auth.views.LoginView`.
    pass

@login_required
def chat_home(request):
    # Show list of all users, a collapsible menu, etc.
    all_users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/chat_home.html', {'all_users': all_users})

@login_required
def chat_room(request, username):
    # Retrieve the chat history between request.user and `username`
    user_to_chat = User.objects.get(username=username)
    messages = Message.objects.filter(
        sender__in=[request.user, user_to_chat],
        receiver__in=[request.user, user_to_chat]
    ).order_by('timestamp')
    return render(request, 'chat/chat_room.html', {
        'user_to_chat': user_to_chat,
        'messages': messages
    })
