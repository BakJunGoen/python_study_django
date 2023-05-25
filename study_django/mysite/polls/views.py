from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views import View
from django.utils import timezone

from .models import Question, Choice
from .models import KakaoFriend

from django.core.serializers import serialize
import json



def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    #위 와 같은 코드
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)
# Create your views here.

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exit")
    # return render(request, 'polls/detail.html', {'question': question})
    # 위와 같은 코드 아래와
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question' : question})



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question' : question,
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})



class IndexView(View):
    def get(self, request):
        friends = KakaoFriend.objects.all().order_by('-id')
        data = json.loads(serialize('json', friends))
        return JsonResponse({'items': data})

    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            friend = KakaoFriend(name = request['name'],
                                 type = request['type'],
                                 job = request['job'],
                                 age = request['age'])
        else:
            friend = KakaoFriend(name = request.POST['name'],
                                 type = request.POST['type'],
                                 job = request.POST['job'],
                                 age = request.POST['age'])
        friend.save()
        return HttpResponse(status=200)
    
    def put(self, request):
        request = json.loads(request.body)
        id = request['id']
        age = request['age']
        friend = get_object_or_404(KakaoFriend, pk=id)
        friend.age = age
        friend.save()
        return HttpResponse(status=200)

    def delete(self, request):
        request = json.loads(request.body)
        id = request['id']
        friend = get_object_or_404(KakaoFriend, pk=id)
        friend.delete()
        return HttpResponse(status=200)