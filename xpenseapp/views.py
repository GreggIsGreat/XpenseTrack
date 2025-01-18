from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BalanceForm, GoalForm
from .models import Account, Goal


# Create your views here.
def index(request):
    account = get_object_or_404(Account, id=1)
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'xpenseapp/index.html', {'account': account, "goals": goals})


def reports(request):
    return render(request, 'xpenseapp/reports.html')


def tradePortfolio(request):
    return render(request, 'xpenseapp/tradePortfolio.html')


def currentGoals(request):
    return render(request, 'xpenseapp/currentGoals.html')


from django.shortcuts import get_object_or_404


def update_balance(request):
    print("Form submitted!")
    account = get_object_or_404(Account, id=1)
    if request.method == 'POST':
        form = BalanceForm(request.POST, instance=account)  # Pass the existing account instance
        if form.is_valid():
            balance_value = form.cleaned_data['balance']
            print(f"Balance updated to: {balance_value}")
            form.save()
            print("Form saved successfully!")
            return redirect('index')
    else:
        form = BalanceForm(instance=account)  # Load the existing account instance
    return render(request, 'xpenseapp/balance_form.html', {'form': form, 'account': account})


# def create_goal(request):
#     if request.method == 'POST':
#         form = GoalForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')  # Redirect to goals table after submission
#     else:
#         form = GoalForm()
#
#     return render(request, 'xpenseapp/create_goal.html', {'form': form})


def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user  # Ensure user is associated
            goal.save()
            messages.success(request, 'Goal created successfully!')
            return redirect('index')
    else:
        form = GoalForm()

    return render(request, 'xpenseapp/create_goal.html', {'form': form})


def goals_table(request):
    account = get_object_or_404(Account, id=1)
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'xpenseapp/goals_table.html', {'goals': goals, "account": account})


def delete_goal(request, pk):
    goal = Goal.objects.get(pk=pk)
    goal.delete()
    return redirect('index')


def edit_goal(request, pk):
    goal = Goal.objects.get(pk=pk)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'xpenseapp/create_goal.html', {'form': form})
