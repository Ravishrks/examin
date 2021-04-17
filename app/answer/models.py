from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
from django.utils.text import slugify
from question.models import Question

# If choice 1st is correct, then result field will store 1, if choce 3rd is correct, it will store 3 and so on.

class SingleChoice(models.Model):
    choice_first = models.CharField(max_length=300, null= True)
    choice_second = models.CharField(max_length=300, null= True)
    choice_third = models.CharField(max_length=300, null= True)
    choice_forth = models.CharField(max_length=300, null= True)
    result = models.IntegerField(blank=True, null=True, default=0)


# If choice 1st only is correct, then result field will store 1000, if 3rd and 4th are correct, it will store 0034 and so on.

class MultipleChoice(models.Model):
    choice_first = models.CharField(max_length=300, null= True)
    choice_second = models.CharField(max_length=300, null= True)
    choice_third = models.CharField(max_length=300, null= True)
    choice_forth = models.CharField(max_length=300, null= True)
    result = models.IntegerField(blank=True, null=True, default=0000)


class IntegerChoice(models.Model):
    result = models.IntegerField(blank=True, null=True, default=0)


class ProgrammeChoice(models.Model):

    # Tells about sample input instructions
    input_format = RichTextUploadingField(blank=True, null=True)

    # Tells about expected output
    expected_output = RichTextUploadingField(blank=True, null=True)

    # inputs to check validity of answer and several other case schenerio to check output
    answer_case_input = models.CharField(max_length=300, null= True)
    test_case_input_first = models.CharField(max_length=300, null= True)
    test_case_input_second = models.CharField(max_length=300, null= True)
    test_case_input_third = models.CharField(max_length=300, null= True)

    # Output to check validity based on case input
    answer_case_output = models.CharField(max_length=300, null= True)
    test_case_output_first = models.CharField(max_length=300, null= True)
    test_case_output_second = models.CharField(max_length=300, null= True)
    test_case_output_third = models.CharField(max_length=300, null= True)

class DatabaseChoice(models.Model):
    # Tells about result output after database operation
    result_output = RichTextUploadingField(blank=True, null=True)


# Each question can associate with single answer only, and answer will be checked based on question type and rest field will be null.

class Answer(models.Model):

    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    single_choice = models.ForeignKey(SingleChoice, on_delete=models.CASCADE, null=True, blank=True)
    multiple_choice = models.ForeignKey(MultipleChoice, on_delete=models.CASCADE, null=True, blank=True)
    integer_choice = models.ForeignKey(IntegerChoice, on_delete=models.CASCADE, null=True, blank=True)
    programme_choice = models.ForeignKey(ProgrammeChoice, on_delete=models.CASCADE, null=True, blank=True)
    database_choice = models.ForeignKey(DatabaseChoice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.pk} | {self.question.title}'