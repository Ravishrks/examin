from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
from django.utils.text import slugify

class Answer(models.Model):
    pass


class SingleChoice(models.Model):
    pass


class MultipleChoice(models.Model):
    pass


class IntegerChoice(models.Model):
    pass


class ProgrammeChoice(models.Model):
    pass


class DatabaseChoice(models.Model):
    pass