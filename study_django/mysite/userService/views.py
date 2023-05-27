from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from django.core.serializers import serialize

# from .models import Users


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def signUp(request):
#     if request.method == "GET":
#         return HttpResponse("signUp")
#         # users = Users.objects.all().order_by('-id')
#         # data = json.loads(serialize('json', Users))
#         # return JsonResponse({'items': data})
    
#     elif request.method == "POST":
#         if request.META['CONTENT_TYPE'] == 'application/json':
#             userNew = Users(user_id = request['user_id'],
#                         user_name = request['user_name'],
#                         user_email = request['user_email'],
#                         user_pw = request['user_pw'],
#                         user_is_staff = request['user_is_staff'],
#                         user_last_login = request['user_last_login'],
#                         user_register_dttm = request['user_register_dttm'])
#         else:
#             userNew = Users(user_id = request.POST['user_id'],
#                         user_name = request.POST['user_name'],
#                         user_email = request.POST['user_email'],
#                         user_pw = request.POST['user_pw'],
#                         user_is_staff = request.POST['user_is_staff'],
#                         user_last_login = request.POST['user_last_login'],
#                         user_register_dttm = request.POST['user_register_dttm'])
#     userNew.save()
#     return HttpResponse(status=200)

# @csrf_exempt
# def signIn(request):
#     if request.method == "GET":
#         return HttpResponse("signUp")
    
#     if request.method == "POST":
#         user_email = request.POST['user_email']
#         user_pw = request.POST['user_pw']

#         user authenticate

#         if 
    

# class userControl(View):

    # if request.META['CONTENT_TYPE'] == 'application/json':
    #     request = json.loads(request.body)
    #     users = User(user_id = request['user_id'],
    #                     user_name = request['user_name'],
    #                     user_email = request['user_email'],
    #                     user_pw = request['user_pw'],
    #                     user_is_staff = request['user_is_staff'],
    #                     user_last_login = request['user_last_login'],
    #                     user_register_dttm = request['user_register_dttm'])
    # else:
    #     users = User(user_id = request.POST['user_id'],
    #                     user_name = request.POST['user_name'],
    #                     user_email = request.POST['user_email'],
    #                     user_pw = request.POST['user_pw'],
    #                     user_is_staff = request.POST['user_is_staff'],
    #                     user_last_login = request.POST['user_last_login'],
    #                     user_register_dttm = request.POST['user_register_dttm'])
        
    # users.save

