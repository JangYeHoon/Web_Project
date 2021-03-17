from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .userdto import UserSerializer
from .models import User

# 회원가입 완료. 새로운 유저 추가
@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# 테스트를 위한 유저 목록 출력
@api_view(['GET'])
def userList(reqeust):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

# 로그인시 아이디와 패스워드가 맞는지 체크하는 함수
@api_view(['PUT'])
def loginCheck(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        json = JSONRenderer().render(serializer.data)
        user = User.objects.get(email = serializer.data['email'])
        if serializer.data['password'] == user.password:
            request.session['email'] = user.email
            return Response(serializer.data)
    return Response('Failed')

    # 로그인이 안된 상태로 예약을 하면 로그인하고 예약을 추가하는 로직
    # 여기서 말고 air_app에서 하는게 좋을거 같아 수정 필요
    # forward_reservaion = request.POST['forward_reservaion']
    # request.session['login_id'] = user_id
    # if forward_reservaion == '1':
    #     context = UserService().reservation_login(user_id, request)
    #     return render(request, 'reservation_complete.html', context)
    # else:
        # return HttpResponseRedirect('/')

# 로그아웃 함수, 세션 삭제
@api_view(['GET'])
def logout(request):
    request.session.modidied = True
    del request.session['login_id']
    return Response("Logout!!")

# 회원가입시 중복 확인하는 함수
@api_view(['GET'])
def id_overlap_check(request, email):
    try:
        user = User.objects.get(email = email)
        return Response("fail")
    except:
        return Response("pass")
