from django.db import models
from user_app.models import User

# Create your models here.
class Board(models.Model):
    objects = models.Manager()
    board_name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    board_writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="board_writer")
    read_count = models.IntegerField()
    write_date = models.DateTimeField()
    contents = models.TextField()
    group = models.IntegerField()
    depth = models.CharField(max_length=30)

class Comment(models.Model):
    objects = models.Manager()
    product_title = models.CharField(max_length=40)
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_writer")
    write_time = models.DateTimeField()
    contents = models.TextField()
    c_list = models.IntegerField()
    c_level = models.CharField(max_length=100)
