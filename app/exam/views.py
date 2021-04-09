from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse




def instructions(request):
    return render(request, 'exam/instructions.html')

def question(request):
    return render(request, 'exam/question.html')

def section(request):
    return render(request, 'exam/section.html')

