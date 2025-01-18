from django.shortcuts import render


def contact(request):
    return render(request, 'forthe50/contact.html')


def index(request):
    return render(request, 'forthe50/index.html')


def team(request):
    return render(request, 'forthe50/team.html')


def statistics(request):
    return render(request, 'forthe50/statistics.html')
