from django.shortcuts import HttpResponse, redirect

# Create your views here.


def hellow_view(request):
    if request.method == 'GET':
        return HttpResponse('hello, its my first view')


def redirect_to_youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com/')



def redirect_to_github_view(request):
    if request.method == 'GET':
        return redirect('https://github.com/t-karina2001')
