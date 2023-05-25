from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def string_response(request):
    return HttpResponse('this is the  first string response')

def string1_response(request):
    return HttpResponse('this is the second string response')


def first_html(request):
    return render(request,'first.html')


def second_html(request):
    return render(request,'second.html')