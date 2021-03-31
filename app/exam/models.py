from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
from django.utils.text import slugify

class QuestionSet(models.Model): 
    pass


class Exam(models.Model): 
    pass
