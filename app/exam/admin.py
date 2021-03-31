from django.contrib import admin
from .models import QuestionSet, Exam

# Register your models here.

admin.site.register(QuestionSet)
admin.site.register(Exam)