from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


from exam.models import QuestionSection, QuestionSet
from question.models import Question
from exam.models import Exam, SetExam, ExamStatus
from result.models import ResponseSheet
from user.models import Profile



def instructions(request):
    return render(request, 'exam/instructions.html')

def question(request, pk):

    # Individual question view
    my_question = Question.objects.get(pk=pk)


    # Get current exam, from setExam database
    current_exam = SetExam.objects.last().exam
    exam_id = current_exam.pk
    

    # Get question set, first element is default 
    question_sets = current_exam.question_set.all()[0]

    # Get question section to have questions inside it
    question_sections = question_sets.question_section.all() 

    # Calculate no of questions and keep on eye on current
    # question index

    questions = []
    index = 0

    # to keep eye on navigation
    question_index = 0

    for i in question_sections:
        for j in i.question.all():
            questions += [j]
            
            index += 1

            if j.pk == pk:
                question_index = index

    # Help to setup 1st question from instruction page
    first_question_index = questions[0].pk


    

    context = {
        # "sections":question_sections,
        "questions":questions,
        "my_question":my_question,
        "current_question_index":question_index,
        "first_question_index":first_question_index,
        "index":index,
        "exam_id":exam_id,

    }

    return render(request, 'exam/question.html', context)

@method_decorator(csrf_exempt, name='dispatch')
class SaveResponse(View):

    def get(self, request):        
        return HttpResponse("Nothing...")

    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        my_data = {
            'username':data['username'],
            'exam_pk':data['examId'],
            'question_pk':data['questionId'],
            'response_data':data['editorContent']
        }

        # Getting particular question to associate response entry
        question = Question.objects.get(pk=my_data['question_pk'])
        print(question)

        # Getting exam status field to maintain status
        exam_status = ExamStatus.objects.filter(exam__pk = my_data['exam_pk'])
        exam_status = exam_status.get(profile__user__username = my_data['username'])
        print(exam_status)

        # Getting Response sheet to save response
        response_sheet = ResponseSheet.objects.filter(exam__pk = my_data['exam_pk'])
        response_sheet = response_sheet.filter(profile__user__username = my_data['username'])

        # Getting common database elements, used during object creation
        my_profile = Profile.objects.get(user__username = my_data['username'])
        my_exam = Exam.objects.get(pk = my_data['exam_pk'])
        my_question = Question.objects.get(pk = my_data['question_pk'])

        

        try:

            # Update respone sheet, if entry is already available
            response_sheet = response_sheet.get(question__pk = my_data['question_pk'])
            response_sheet.response = my_data['response_data']
            response_sheet.save()


        except ResponseSheet.DoesNotExist:

            # Create response sheet for a particular question
            # Newline (\n) is preserved in database, checked
            rs = ResponseSheet(profile = my_profile, exam = my_exam, question = my_question, response = my_data['response_data'])
            rs.save()

        # note: create ExamStutus entry 

        
        return HttpResponse("Answer saved")


 

# save response to database

def all_questions(request):

    current_exam = SetExam.objects.last().exam
    question_sets = current_exam.question_set.all()[0]
    question_sections = question_sets.question_section.all() 

    # Calculate no of questions and keep on eye on current
    # question index

    questions = []

    for i in question_sections:
        for j in i.question.all():
            questions += [j]
            

    context = {
        "questions":questions,
        "page_all_question":"page_all_question",

    }
    return render(request, 'exam/all-questions.html', context)

def section(request):
    return render(request, 'exam/section.html')

