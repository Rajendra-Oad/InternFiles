from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(self):
	return HttpResponse("Welcome user")
