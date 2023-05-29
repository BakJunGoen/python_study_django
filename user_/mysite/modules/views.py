from django.shortcuts import render


from django.http import HttpResponse, JsonResponse

#csrf 풀기
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from django.views import View

import json

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

        
    # if request.method == "GET":
    #     return HttpResponse("signUp 호출")
    return HttpResponse(status=200)



@method_decorator(csrf_exempt, name='dispatch')
class singup2(View):
    def get(self, request):
        return HttpResponse(status=200)

    def post(self, request):
        data = json.loads(request.body)
        signup_data = User.objects.all()
        print(data['id'])
        try:
            user = User(
                password = data['password'],
                username = data['username'],
                email = data['email'],
                is_staff = data['is_staff'],
                is_active = data['is_active'],
                last_login = timezone.now()
            )
            user.full_clean()

            if signup_data.filter(username = data['username']).exists() :
                return JsonResponse({'message': 'username  : already exists'}, status=200)

            user.save()
            return JsonResponse({'message': 'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'} , status= 200)



# @csrf_exempt
# def signIn(request):
#     if request.method == "POST":
        


# # Create your views here.
