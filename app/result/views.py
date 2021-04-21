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
    
    # testing with one entry
    print(my_response_sheet)

    for sheet in my_response_sheet:

    # sheet = my_response_sheet.first()
        new_file = f'{sheet.pk}{sheet.exam.pk}{sheet.question.pk}{sheet.profile.user.username}'

        my_programme = sheet.response

        # taking decision based on programme type
        if sheet.question.question_type == "Programme":

            my_language_type = sheet.language_type[1:]
            programe_file_location = f'result/program/{my_language_type}/files/{new_file}{sheet.language_type}'
            output_file_location = f'result/program/{my_language_type}/output/{new_file}{sheet.language_type}.txt'
            error_file_location = f'result/program/{my_language_type}/error/{new_file}{sheet.language_type}.txt'
            sh_file_location = f'result/program/{my_language_type}/sh/{new_file}{sheet.language_type}.sh'


            if sheet.language_type == ".js":
                print("It's js bro")

                with open(programe_file_location, 'w') as f:
                    f.write(my_programme)

                # create shell script files
                with open(sh_file_location, 'w') as sh:
                    shell_cmd = f'#!/bin/sh\nnode {programe_file_location} > {output_file_location}\nnode {programe_file_location} 2> {error_file_location}'
                    sh.write(shell_cmd)

                subprocess.run(["chmod","777",sh_file_location])    
                subprocess.run(["chmod","777",programe_file_location])    
                subprocess.run(["chmod","777",output_file_location])    
                subprocess.run(["chmod","777",error_file_location])    
                subprocess.run([sh_file_location]) 
                

                # Save output or error to response file 

                with open(output_file_location) as rf:
                    read_file = rf.read()
                    sheet.output = read_file
                    sheet.save()
                      

                with open(error_file_location) as ef:
                    read_file_error = ef.read()
                    sheet.error = read_file_error
                    sheet.save()   

            elif sheet.language_type == ".c":
                print("It's c bro")  

            elif sheet.language_type == ".cpp":
                print("It's c++ bro")  

            elif sheet.language_type == ".py":
                print("It's python bro")  

            elif sheet.language_type == ".php":
                print("It's php bro")  
            elif sheet.language_type == ".java":
                print("It's java bro")  


    return HttpResponse("Checked!")

