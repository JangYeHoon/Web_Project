from django.forms import ModelForm
from .models import Board, Comment

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = {'board_name', 'title', 'board_writer', 'read_count',
        'write_date', 'contents', 'group', 'depth'}

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = {'product_title', 'comment_writer', 'write_time', 'contents', 'c_list', 'c_level'}