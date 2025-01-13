from django.db import models
from django.contrib.auth.models import User


# User Profile
class User1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    current_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# Transaction
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Income', 'Income'),
        ('Expense', 'Expense')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Completed')

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"


# Budget
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    month = models.DateField()

    def __str__(self):
        return f"Budget for {self.category}"


# Goal
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    timeline = models.DateField()
    required_savings = models.DecimalField(max_digits=10, decimal_places=2)
    progress = models.PositiveIntegerField()
    complete = models.BooleanField(default=False)
    priority = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Expense Distribution
class ExpenseDistribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount}"


# Expense Trend
class ExpenseTrend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    change_percentage = models.FloatField()

    def __str__(self):
        return f"Trend for {self.month}"


# Order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_name = models.CharField(max_length=100)
    order_date = models.DateField()
    status = models.CharField(max_length=20, default='Pending')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_name


# Settings
class Settings(models.Model):
    THEME_CHOICES = (
        ('Light', 'Light'),
        ('Dark', 'Dark')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default='Light')
    notifications_enabled = models.BooleanField(default=True)
    currency = models.CharField(max_length=5, default='USD')

    def __str__(self):
        return f"Settings for {self.user.user.username}"


class Account(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
