from django.shortcuts import render, redirect
from .forms import BalanceForm
from .models import Account


# Create your views here.
def index(request):
    return render(request, 'xpenseapp/index.html')


def reports(request):
    return render(request, 'xpenseapp/reports.html')


def tradePortfolio(request):
    return render(request, 'xpenseapp/tradePortfolio.html')


def currentGoals(request):
    return render(request, 'xpenseapp/currentGoals.html')


from django.shortcuts import get_object_or_404


def update_balance(request):
    account = get_object_or_404(Account, id=1)
    if request.method == 'POST':
        form = BalanceForm(request.POST, instance=account)  # Pass the existing account instance
        if form.is_valid():
            form.save()
            return redirect('account_detail')
    else:
        form = BalanceForm(instance=account)  # Load the existing account instance
    return render(request, 'xpenseapp/balance_form.html', {'form': form, 'account': account})
