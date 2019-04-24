from django.shortcuts import render
from django.http import HttpResponse
from aulaDjango import*

def index(request):
	return render(request,'index.html')
