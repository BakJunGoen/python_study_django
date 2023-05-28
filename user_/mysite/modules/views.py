from django.shortcuts import render


from django.http import HttpResponse

#csrf 풀기
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import User

def index(request):
    return HttpResponse("/modules 의 index 입니다.")

# csrf 보안 해제(test할때만 풀것)
@csrf_exempt 
def signUp(request):

    ''' signUp 회원가입
        password,
        username,
        emial,
        is_staff,
        is_active,
        의 데이터를 받음'''
    
    if request.method == "GET":
        return HttpResponse("signUp 함수")
    
    if request.method == "POST":
        if request.META['CONTENT_TYPE'] == 'application/json':
            userNew = User(
                        password = request['password'],
                        username = request['username'],
                        email = request['email'],
                        is_staff = request['is_staff'],
                        is_active = request['is_active'],
                        last_login = timezone.now()
                        )
        else:
            userNew = User(
                        password = request.POST['password'],
                        username = request.POST['username'],
                        email = request.POST['email'],
                        is_staff = request.POST['is_staff'],
                        is_active = request.POST['is_active'],
                        last_login = timezone.now()
                        )
    userNew.save()
    return HttpResponse(status=200)



# Create your views here.
