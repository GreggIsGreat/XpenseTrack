from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'xpenseapp/index.html')


def reports(request):
    return render(request, 'xpenseapp/reports.html')


def tradePortfolio(request):
    return render(request, 'xpenseapp/tradePortfolio.html')


def currentGoals(request):
    return render(request, 'xpenseapp/currentGoals.html')
