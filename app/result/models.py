from django.db import models
from user.models import Profile
from exam.models import Exam
from question.models import Question
from ckeditor.fields import RichTextField


# Create your models here.


# store response for each question (Based on question type), whether, it is mcq, database, programming etc. 
class ResponseSheet(models.Model):

    LANGUAGE = (
        ('.js', 'javascript'),
        ('.c', 'c'),
        ('.cpp', 'c++'),
        ('.py', 'python'),
        ('.php', 'php'),
        ('.java', 'java'),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = RichTextField(blank=True, null=True, editable=False)
    language_type = models.CharField(max_length=30, choices=LANGUAGE, blank=True, null=True)
    output = RichTextField(blank=True, null=True, )
    error = RichTextField(blank=True, null=True, )


    def __str__(self):
        return f'{self.pk} | {self.profile.user.username}'


# Will be created based on Response sheet
class AnswerSheet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)
    correct_questions = models.ManyToManyField(Question, related_name = "correct_questions", blank=True)
    incorrect_questions = models.ManyToManyField(Question, related_name = "incorrect_questions", blank=True)
    unattempted_questions = models.ManyToManyField(Question, related_name = "unattempted_questions", blank=True)
    marks_obtained = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f'{self.pk} | {self.profile.user.username}'

#  Will be calculated based on Answersheet
class Result(models.Model):
    is_qualified = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)
    answer_sheet = models.OneToOneField(AnswerSheet, on_delete=models.CASCADE)
    total_marks = models.IntegerField(blank=True, null=True, default=0)
    note = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.pk} | {self.profile.user.username}'