from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse

from exam.models import QuestionSection, QuestionSet
from question.models import Question
from exam.models import Exam, SetExam



def instructions(request):
    return render(request, 'exam/instructions.html')

def question(request, pk):

    # Individual question view
    my_question = Question.objects.get(pk=pk)


    # Get current exam, from setExam database
    current_exam = SetExam.objects.last().exam

    # Get question set, first element is default 
    question_sets = current_exam.question_set.all()[0]

    # Get question section to have questions inside it
    question_sections = question_sets.question_section.all() 

    # Calculate no of questions and keep on eye on current
    # question index

    questions = []
    index = 0
    question_index = 0

    for i in question_sections:
        for j in i.question.all():
            questions += [j]
            
            index += 1

            if j.pk == pk:
                question_index = index

    first_question_index = question[0].pk


    

    context = {
        # "sections":question_sections,
        "questions":questions,
        "my_question":my_question,
        "current_question_index":question_index,
        "first_question_index":first_question_index,
    }

    return render(request, 'exam/question.html', context)

def all_questions(request):
    return render(request, 'exam/all-questions.html')

def section(request):
    return render(request, 'exam/section.html')

