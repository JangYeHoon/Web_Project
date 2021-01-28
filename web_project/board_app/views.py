from django.shortcuts import render
from .forms import BoardForm,CommentForm
from .services import BoardService
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.
def board_list(request):
    content = BoardService().board_list(request)
    return render(request, 'board_list.html', content)

def board_input(request):
    user_id = request.session.get('login_id')
    if user_id == 'admin@admin.com' and request.POST.get('board_id'):
        content = BoardService().board_input(request)
        return render(request, 'board_input.html', content)
    else:
        return render(request, 'board_input.html')

def board_add(request):
    input_value = BoardForm(request.POST)
    BoardService().board_add(request, input_value)
    return HttpResponseRedirect(reverse('board_list'))

def board_view(request):
    content = BoardService().board_view(request)
    return render(request, 'board_view.html', content)

def board_modify_input(request):
    content = BoardService().board_modify_input(request)
    return render(request, 'board_modify.html', content)

def board_modify(request):
    BoardService().board_modify(request)
    return HttpResponseRedirect(reverse('board_list'))

def board_delete(request):
    board_id = request.POST['board_id']
    BoardService().board_delete(board_id)
    return HttpResponseRedirect(reverse('board_list'))

def comment_add(request):
    input_value =CommentForm(request.POST)
    board_id = BoardService().comment_add(request,input_value)
    return HttpResponseRedirect('board_view?board_id='+board_id)

def loginStateCheck(request):
    login =request.session.get('login_id')
    if login is None:
        state={'state':"logout"}
    else :
        state={'state':"login"}
    return JsonResponse(state)

def comment_delete(request):
    board_id = request.POST['board_id']
    comment_id = request.POST['comment_id']
    BoardService().comment_delete(comment_id)
    return HttpResponseRedirect('board_view?board_id='+board_id)