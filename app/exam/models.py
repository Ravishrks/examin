from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
from question.models import Question
from user.models import Profile


# Section to sort questions based on particular section
# i.e mcq, integer, database etc to create paper.
# Various section will contribute to be a question set, and rand field will help to position section.

class QuestionSection(models.Model):

    title = models.CharField(max_length=100, null=True)

    # Will introduce, how this section behaves, as well as marking schemes or any type of general instructions.
    section_instructions = RichTextUploadingField(blank=True, null=True)

    # Will help to priotise questions set in question paper
    rank = models.IntegerField(default=6, blank=True, null=True)

    # particular type of questions added
    question = models.ManyToManyField(Question)

    def __str__(self):
        return f'{self.pk} | {self.title}'
 


class QuestionSet(models.Model): 
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)

    # Each question set consists of various sections

    question_section = models.ManyToManyField(QuestionSection)

    def __str__(self):
        return f'{self.pk} | {self.title}'    
     




class Exam(models.Model): 
    created_date = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    title = models.CharField(max_length=100) 
    instructions = RichTextUploadingField(blank=True, null=True) 

    # Exam can have multiple question set, first set is default
    question_set = models.ManyToManyField(QuestionSet) 
    note = models.CharField(max_length=100)
    scheduled = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.pk} | {self.title}'


# After adding profiles to ExamSubscriber,
# particular exam will be available to users
class ExamSubscriber(models.Model):
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE, null=True)
    profile = models.ManyToManyField(Profile)


# last added exam will be in live mode
# control which exam to conduct
# Exam id will be generated based on this data.
class SetExam(models.Model):
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE, null=True)


    # Handle status of exam for a particular exam, user
class ExamStatus(models.Model):
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE, null=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    is_submitted = models.BooleanField(default=False)
    total_questions = models.IntegerField(blank=True, null=True, default=0)
    completed_questions = models.IntegerField(blank=True, null=True, default=0)
    time_left = models.IntegerField(blank=True, null=True, default=0)
    saved_response_question = models.ManyToManyField(Question)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)