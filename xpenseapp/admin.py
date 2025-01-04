from django.contrib import admin
from .models import UserProfile, Transaction, Budget, Goal, ExpenseDistribution, ExpenseTrend, Order, Settings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Inline UserProfile for User Admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'


# Extend User Admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)


# Register User Admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register other models
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_type', 'amount', 'category', 'date', 'status')
    search_fields = ('user__user__username', 'category', 'status')
    list_filter = ('transaction_type', 'date', 'status')


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'allocated_amount', 'spent_amount', 'remaining_amount', 'month')
    search_fields = ('user__user__username', 'category')
    list_filter = ('month',)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal_name', 'target_date', 'required_savings', 'current_progress', 'completed')
    search_fields = ('user__user__username', 'goal_name')
    list_filter = ('completed', 'priority', 'target_date')


@admin.register(ExpenseDistribution)
class ExpenseDistributionAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'month')
    search_fields = ('user__user__username', 'category')
    list_filter = ('month',)


@admin.register(ExpenseTrend)
class ExpenseTrendAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'total_expenses', 'change_percentage')
    search_fields = ('user__user__username',)
    list_filter = ('month',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_name', 'order_date', 'status', 'amount')
    search_fields = ('user__user__username', 'order_name', 'status')
    list_filter = ('order_date', 'status')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'theme', 'notifications_enabled', 'currency')
    search_fields = ('user__user__username', 'currency')
    list_filter = ('theme', 'notifications_enabled')


from django.contrib import admin

# Register your models here.
