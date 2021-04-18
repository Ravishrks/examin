from django.contrib import admin
from .models import QuestionSet, Exam, QuestionSection, ExamSubscriber, SetExam, ExamStatus

# Register your models here.

admin.site.register(QuestionSet)
admin.site.register(QuestionSection)
admin.site.register(Exam)
admin.site.register(ExamSubscriber)
admin.site.register(SetExam)
admin.site.register(ExamStatus)