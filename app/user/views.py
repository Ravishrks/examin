from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .form import RegisterAccount
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from user.models import Profile

 

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


def dashboard(request):
    return render(request, 'user/dashboard.html')

def profile(request):
    return render(request, 'user/profile.html')


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['avatar', 'college', 'course', 'session_start', 'session_end', 'phone', 'address', 'aadhar', 'birthday', 'gender']
    template_name = 'user/profile_update_form.html'

def payment(request):
    return render(request, 'user/payment.html')

def feedback(request):
    return render(request, 'user/feedback.html')

def notifications(request):
    return render(request, 'user/notifications.html')

def error(request):
    return render(request, 'user/error.html')

def success(request):
    return render(request, 'user/success.html')