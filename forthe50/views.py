from django.shortcuts import render

# Create your views here.


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')


def team(request):
    return render(request, 'team.html')


def report(request):
    return render(request, 'report.html')