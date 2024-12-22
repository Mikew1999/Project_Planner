from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from Users.user_auth import process_login

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "Main/login.html")

    username = request.POST.get("username", "")
    pw = request.POST.get("password", "")
    # todo get redirect

    user = process_login(request, username, pw)
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid username or password")
        return render(request, "Main/login.html")
    
    return redirect("/Projects/")
