from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def contacts(request):
    return render(request, 'home/contacts.html')


def about(request):
    return render(request, 'home/about.html')