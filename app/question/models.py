from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
from django.utils.text import slugify
from answer.models import Answer

# Store questions, with type of questions, so as to process question based on type. Type will help to process question while generating results.

class Question(models.Model):
    TYPES = (
        ('Single', 'Single Choice'),
        ('Mutiple', 'Multiple Choice'),
        ('Integer', 'Integer'),
        ('Programme', 'Programming'),
        ('Database', 'Database Operations'),
    )

    DIFFICULTY = (
        ('Easy', 'Easy'),
        ('Normal', 'Normal'),
        ('Hard', 'Hard'),
        ('Expert', 'Expert')
    )

    title = models.CharField(max_length=100)
    question_type = models.CharField(max_length=20, choices=TYPES, null=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    weitage = models.IntegerField(blank=True, null=True, default=0)
    created_date = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)    

    def __str__(self):
        return f'{self.tite}'


