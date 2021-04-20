from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from result.models import ResponseSheet
import os
import subprocess





def result(request):
    return render(request, 'user/dashboard.html')


def checkResponseSheet(request, exam_id):

    my_response_sheet = ResponseSheet.objects.filter(exam__pk = exam_id)
    print(my_response_sheet)

    # testing with one entry

    sheet = my_response_sheet.first()
    my_programme = sheet.response
    # print(sheet.pk)

    cwd = os.getcwd()
    

    # Generate unique file name, answersheet pk, exam id, profile id, question id and language extension

    with open('result/programme-files/program/workfile.js', 'w') as f:
        print("inside file")
        f.write(my_programme)

    # subprocess.run(["node", "result/programme-files/program/workfile.js", ">", "result/programme-files/output/workfile.txt"])
    subprocess.run(["./result/programme-files/program/test.sh"])


    # outfile file
    # with open('result/programme-files/program/workfile.js', 'w') as f:
    #     print("inside file")
    #     f.write(my_programme)

    return HttpResponse("Checked!")

