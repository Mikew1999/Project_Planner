from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def process_login(request, username: str, password: str) -> User | None:

    users = User.objects.all()
    for user in users:
        print(user.__dict__)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return None
    
    login(request, user)

    return user
