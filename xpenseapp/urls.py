from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('reports', views.reports, name='reports'),
    path('tradePortfolio', views.tradePortfolio, name='tradePortfolio'),
    path('currentGoals', views.currentGoals, name='currentGoals'),
    path('update_balance/', views.update_balance, name='update_balance'),
    path('goals/', views.goals_table, name='goals_table'),
    path('goals/create/', views.create_goal, name='create_goal'),
    path('goals/<int:pk>/delete/', views.delete_goal, name='delete_goal'),
    path('goals/<int:pk>/edit/', views.edit_goal, name='edit_goal'),
    path('login/', auth_views.LoginView.as_view(template_name='xpenseapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),

]