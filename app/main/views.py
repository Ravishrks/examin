from django.shortcuts import render
from django.http import HttpResponse, Http404



def index(request):

    context = { 
        "published":"page_obj",  
    }

    return render(request, 'main/index.html', context)



def robots(request):
    return render(request, 'main/robots.txt' , content_type='text/plain')