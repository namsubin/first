from email.policy import default
from enum import unique
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    like_count = models.PositiveIntegerField(default=0) # 양수입력 필드
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Reply(models.Model):
    reply = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rep_date = models.DateTimeField()

    def __str__(self):
        return self.comment