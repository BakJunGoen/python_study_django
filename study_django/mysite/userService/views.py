from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from django.core.serializers import serialize
# from models import Question
# from models import User

# class IndexView(View):
    # def get(self, request):
    #     dummy_data = {
    #         'name': '죠르디',
    #         'type': '공룡',
    #         'job': '편의점알바생',
    #         'age': 5
    #     }
    #     return JsonResponse(dummy_data)


    # def get(self, request):
    #     dummy_data = {
    #         'name' : '조르디',
    #         'type' : '공룡'
    #     }

    #     return JsonResponse(dummy_data)


    # def post(self, request):
    #     if request.META['CONTENT_TYPE'] == 'application/json':
    #         request = json.loads(request.body)
    #         question = Question(question_text = request['question_text'],
    #                             pub_date = request['pub_date'])
            
    #     else:
    #         question = Question(question_text = request.POST['question_text'],
    #                             pub_date = request.POST['pub_date'])

    #     question.save

    #     return HttpResponse(status='200')






    # def post(self, request):
        
        # if request.META['CONTENT_TYPE'] == 'application/json':
        #     request = json.loads(request.body)
        #     users = User(user_id = request['user_id'],
        #                  user_name = request['user_name'],
        #                  user_email = request['user_email'],
        #                  user_pw = request['user_pw'],
        #                  user_is_staff = request['user_is_staff'],
        #                  user_last_login = request['user_last_login'],
        #                  user_register_dttm = request['user_register_dttm'])
        # else:
        #     users = User(user_id = request.POST['user_id'],
        #                  user_name = request.POST['user_name'],
        #                  user_email = request.POST['user_email'],
        #                  user_pw = request.POST['user_pw'],
        #                  user_is_staff = request.POST['user_is_staff'],
        #                  user_last_login = request.POST['user_last_login'],
        #                  user_register_dttm = request.POST['user_register_dttm'])
            
        # users.save

        # return HttpResponse(status=200)
