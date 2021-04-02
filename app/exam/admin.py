from django.contrib import admin
from .models import QuestionSet, Exam, QuestionSection

# Register your models here.

admin.site.register(QuestionSet)
admin.site.register(QuestionSection)
admin.site.register(Exam)