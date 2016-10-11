from django.shortcuts import render
#from django.http import HttpResponse

#def home(request):
#	return HttpResponse('<h1>Django</h1><h3>Bem-vindo ao .NET Coders!</h3>')

# Create your views here.

def home(request):
    return render(request, 'index.html')
