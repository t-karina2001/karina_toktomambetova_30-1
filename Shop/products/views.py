from django.shortcuts import HttpResponse
import datetime

# Create your views here.


def hellow_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def date_view(request):
    if request.method == 'GET':
        date = datetime.date.today()
        return HttpResponse(f'Today {date}')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
