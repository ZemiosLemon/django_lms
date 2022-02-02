from django.http import HttpResponse
from django.shortcuts import render

def index(requist):
    return HttpResponse('<h1> HELLO!!! </h1>')
