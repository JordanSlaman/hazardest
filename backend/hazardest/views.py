from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, "root/index.html")

@login_required
def play(request):
    return render(request, "play/index.html")