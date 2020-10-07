from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Vocabulary(models.Model):
    word = models.TextField(max_length=100)
    phonetic_symbols = models.TextField(max_length=100)
    mean = models.TextField(max_length=200)
    Toeic = models.BooleanField()
    Opic = models.BooleanField()
    korean_SAT = models.BooleanField()

class Speaking(models.Model):
    image = models.ImageField()
    cap_text = models.TextField()

class Listening(models.Model):
    sound = models.FileField()
    extraction_text = models.TextField()

class Userwordbook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.TextField(max_length=100)
    phonetic_symbols = models.TextField(max_length=100)
    mean = models.TextField(max_length=200)