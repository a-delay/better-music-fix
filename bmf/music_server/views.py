from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    	return render(request,'homepage.html')
	#return HttpResponse("music server index! hello world")

def player(request):
	return render(request, 'player.html')
