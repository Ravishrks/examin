from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .form import RegisterAccount
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from article.models import Bookmark
from author.models import Author
from django.http import HttpResponse

 

class Register(View):
    template_register = 'user/register.html'
    template_error = 'user/error.html'
    template_success = 'user/success.html'

    def post(self, request):
        form = RegisterAccount(request.POST)

        #get_username = request.POST['username']


        if form.is_valid():
            form.save()
            
            return render(request, self.template_success)
        return render(request, self.template_error)

    def get(self, request):
        form = RegisterAccount()
        return render(request, self.template_register, {'form': form})