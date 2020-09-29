from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    total_point = models.IntegerField(default=0)

class Point(models.Model):
    use_type = models.BooleanField()
    value = models.IntegerField()
    content = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class DateCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    # datetimefield가 아니라 datefield를 사용
    # '날짜'만 비교할 것이기 때문!!!
    image_speak_count = models.IntegerField(default='0')
    vocabulary_count = models.IntegerField(default='0')
    listening_count = models.IntegerField(default='0')