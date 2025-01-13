from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('reports', views.reports, name='reports'),
    path('tradePortfolio', views.tradePortfolio, name='tradePortfolio'),
    path('currentGoals', views.currentGoals, name='currentGoals'),
    path('update_balance/', views.update_balance, name='update_balance'),
    path('goals/', views.goals_table, name='goals_table'),
    path('goals/create/', views.create_goal, name='create_goal'),
]