from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def index(request):
    return render(request, 'index.html')