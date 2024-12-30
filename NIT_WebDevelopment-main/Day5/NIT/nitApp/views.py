from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(self):
	return HttpResponse("welcome to the project")

def sec(req):
	return HttpResponse("<h2 style='background-color:green;color:white'>Welcome to the project</h2>")

def para(req,nm,y,dept):
	return HttpResponse(f"I am {nm} studying {y} year in {dept} department")