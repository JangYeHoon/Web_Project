from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .boarddto import BoardSerializer, CommentSerializer
from .models import Board, Comment

# 게시글 리스트 받아오는 함수
@api_view(['GET'])
def board_list(request):
    boards = Board.objects.all().order_by('group')
    serializer = BoardSerializer(boards, many = True)
    return Response(serializer.data)

# 게시글 추가하는 함수
@api_view(['POST'])
def board_add(request):
    serializer = BoardSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# 게시글 내용 넘겨주는 함수
@api_view(['GET'])
def board_view(request, pk):
    board = Board.objects.get(id=pk)
    board.read_count += 1
    board.save()
    serializer = BoardSerializer(board)
    return Response(serializer.data)

# 수정할 게시글 내용 받아오는 함수
@api_view(['GET'])
def board_modify_input(request, pk):
    board = Board.objects.get(id=pk)
    serializer = BoardSerializer(board)
    return Response(serializer.data)

# 게시글 수정
@api_view(['PUT'])
def board_modify(request, pk):
    board = Board.objects.get(id = pk)
    board.title = request.data['title']
    board.contents = request.data['contents']
    board.save()
    serializer = BoardSerializer(board)
    return Response(serializer.data)

# 게시글 삭제
@api_view(['DELETE'])
def board_delete(request, pk):
    board = Board.objects.get(id = pk)
    if board.depth == '0':
        board_list = Board.objects.filter(group=pk)
        for b in board_list:
            b.delete()
    else:
        board.delete()
    return Response('Deleted')

# 댓글 추가
@api_view(['POST'])
def comment_add(request):
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# 댓글 삭제
@api_view(['DELETE'])
def comment_delete(request, pk):
    comment = Comment.objects.get(id = pk)
    if comment.c_level == '0':
        comment_list = Comment.objects.filter(c_list=comment_id)
        for c in comment_list:
            c.delete()
    else:
        comment.delete()
    return Response('Deleted')