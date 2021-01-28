from .models import Board, Comment
from user_app.models import User
import datetime


class BoardService:
    def board_input(self, request):
        board_id = request.POST['board_id']
        board = Board.objects.get(id=board_id)
        title = "Re: " + board.title
        content = {"board_id": board_id, "title": title}
        return content

    def board_add(self, request, input_value):
        user_id = request.session.get('login_id')

        user = User.objects.get(email=user_id)
        now = datetime.datetime.now()

        board_value = input_value.data['board_name']
        if board_value == '1':
            board_name = '여행후기'
        elif board_value == '2':
            board_name = '고객센터'
        title = input_value.data['title']
        contents = input_value.data['contents']
        if user_id == 'admin@admin.com':
            board_id = input_value.data['board_id']
            new_board = Board(board_name=board_name, title=title, board_writer=user,
                              read_count=0, write_date=now.strftime('%Y-%m-%d %H:%M:%S'), contents=contents, group=board_id, depth='1')
            new_board.save()
        else:
            new_board = Board(board_name=board_name, title=title, board_writer=user,
                              read_count=0, write_date=now.strftime('%Y-%m-%d %H:%M:%S'), contents=contents, group=0, depth='0')
            new_board.save()
            key = Board.objects.latest('id')
            change_board = Board.objects.get(id=key.id)
            change_board.group = key.id
            change_board.save()

    def board_list(self, request):
        board_list = Board.objects.all().order_by('group')
        content = {'board_list': board_list}
        return content

    def board_view(self, request):
        board_id = request.GET['board_id']
        board = Board.objects.get(id=board_id)
        board.read_count += 1
        board.save()
        comment_list = Comment.objects.filter(
            board_id=board_id).order_by('c_list')
        user_id = request.session.get('login_id')
        if user_id:
            if user_id == board.board_writer.email:
                content = {'board': board, 'writer_check': '1',
                           'comment_list': comment_list}
            elif user_id == 'admin@admin.com':
                content = {'board': board, 'writer_check': '2',
                           'comment_list': comment_list}
        else:
            content = {'board': board, 'writer_check': '0',
                       'comment_list': comment_list}

        return content

    def board_modify_input(self, request):
        board_id = request.POST['board_id']
        board = Board.objects.get(id=board_id)
        board_name = '0'
        if board.board_name == '여행후기':
            board_name = '1'
        elif board.board_name == '고객센터':
            board_name = '2'
        content = {'board': board, 'board_name': board_name}
        return content

    def board_modify(self, request):
        board_id = request.POST['board_id']
        board = Board.objects.get(id=board_id)

        board_title = request.POST['title']
        board_contents = request.POST['contents']

        board.title = board_title
        board.contents = board_contents
        board.save()

    def board_delete(self, board_id):
        board_list = Board.objects.filter(group=board_id)
        for board in board_list:
            board.delete()

    def comment_add(self, request, input_value):
        user_id = request.session.get('login_id')
        board_id = input_value.data['board_id']
        user = User.objects.get(email=user_id)
        board = Board.objects.get(id=board_id)
        now = datetime.datetime.now()
        contents = input_value.data['comment_contents']
        c_level = input_value.data['c_level']
        c_list = input_value.data['c_list']

        if c_list == "0":
            new_comment = Comment(comment_writer=user, board_id=board, write_time=now.strftime(
                '%Y-%m-%d %H:%M:%S'), contents=contents, c_list=0, c_level=c_level)
            new_comment.save()
            key = Comment.objects.latest('id')
            change_comment = Comment.objects.get(id=key.id)
            change_comment.c_list = key.id
            change_comment.save()
        else:
            new_comment = Comment(comment_writer=user, board_id=board, write_time=now.strftime(
                '%Y-%m-%d %H:%M:%S'), contents=contents, c_list=c_list, c_level=c_level)
            new_comment.save()
        return board_id

    def comment_delete(self, comment_id):
        level = Comment.objects.get(id=comment_id)
        print(level.c_level)
        if level.c_level == 0:
            comment_list = Comment.objects.filter(c_list=comment_id)
            for comment in comment_list:
                comment.delete()
        else:
            level.delete()
