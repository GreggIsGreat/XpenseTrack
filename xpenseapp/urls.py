from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('reports', views.reports, name='reports'),
    path('tradePortfolio', views.tradePortfolio, name='tradePortfolio'),
    path('currentGoals', views.currentGoals, name='currentGoals'),
]