from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def data(request):
    return render(request, 'pages/data.html')


def analytics(request):
    return render(request, 'pages/analytics.html')
