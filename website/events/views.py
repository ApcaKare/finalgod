from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'events/home.html', {})

def guntur(request):
	return render(request, 'events/guntur.html', {})