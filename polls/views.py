from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5] 
    return render(request, 'polls/index.html', {"latest_question_list":latest_question_list})

def details(request,question_id):
    pass

def results(request, question_id):
    pass

def vote(request, question_id):
    pass
