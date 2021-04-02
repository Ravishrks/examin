from django.db import models
from user.models import Profile
from exam.models import Exam
from question.models import Question

# Create your models here.

class AnswerSheet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)
    correct_questions = models.ManyToManyField(Question, related_name = "correct_questions", blank=True)
    incorrect_questions = models.ManyToManyField(Question, related_name = "incorrect_questions", blank=True)
    unattempted_questions = models.ManyToManyField(Question, related_name = "unattempted_questions", blank=True)
    marks_obtained = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f'{self.profile.user.username}'

class Result(models.Model):
    is_qualified = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)
    answer_sheet = models.OneToOneField(AnswerSheet, on_delete=models.CASCADE)
    total_marks = models.IntegerField(blank=True, null=True, default=0)
    note = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.profile.user.username}'