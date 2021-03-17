from rest_framework import serializers, viewsets
from .models import Board, Comment

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['board_name', 'title', 'board_writer', 'read_count', 'write_date',
            'contents', 'group', 'depth']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_writer', 'board_id', 'write_time', 'contents',
            'contents', 'c_list', 'c_level']