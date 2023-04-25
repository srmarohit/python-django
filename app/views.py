from json import loads
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import ChatMessageForm

from app.models import ChatMessage, Profile, Friend

# Create your views here.


def index(request):
    user = request.user.profile  # it will work only user logged in and having profile
    friends = user.friends.all()
    context = {
        "name": user,
        "friends": friends
    }
    print(friends[0].profile.id)
    return render(request, "mychatapp/index.html", context)


def friend_detail(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    form = ChatMessageForm()
    chats = ChatMessage.objects.all()

    # form submitted
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect("friend_detail", pk=friend.profile.id)

    context = {"friend": friend, "form": form,
               "user": user, "chats": chats, "profile": profile}
    return render(request, "mychatapp/detail.html", context)


def sentMessage(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    data = loads(request.body)

    new_chat = data['msg']
    new_chat_message = ChatMessage.objects.create(body = new_chat, msg_sender = user, msg_receiver = profile, seen = False)
    
    return JsonResponse(new_chat_message.body, safe=False)

