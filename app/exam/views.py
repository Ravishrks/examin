from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse

from exam.models import QuestionSection, QuestionSet
from question.models import Question




def instructions(request):
    return render(request, 'exam/instructions.html')

def question(request):

    question = Question.objects.all().first()

    context = {
        "question":question,
    }

    return render(request, 'exam/question.html', context)

def all_questions(request):
    return render(request, 'exam/all-questions.html')

def section(request):
    return render(request, 'exam/section.html')

