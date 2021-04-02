from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
from question.models import Question


# Section to sort questions based on particular section
# i.e mcq, integer, database etc to create paper.
# Various section will contribute to be a question set, and rand field will help to position section.

class QuestionSection(models.Model):

    # Will introduce, how this section behaves, as well as marking schemes or any type of general instructions.
    section_instructions = body = RichTextUploadingField(blank=True, null=True)

    # Will help to priotise questions set in question paper
    rank = models.IntegerField(default=6, blank=True, null=True)

    # particular type of questions added
    question = models.ManyToManyField(Question)



class QuestionSet(models.Model): 
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)

    # Each question set consists of various sections

    question_section = models.ManyToManyField(QuestionSection)    
     




class Exam(models.Model): 
    created_date = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    title = models.CharField(max_length=100) 
    instructions = RichTextUploadingField(blank=True, null=True) 

    # Exam can have multiple question set, first set is default
    question_set = models.ManyToManyField(QuestionSet) 
    note = models.CharField(max_length=100)
    scheduled = date = models.DateTimeField(blank=True, null=True)


