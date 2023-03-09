from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_create, name='portfolio_create'),
    path('portfolio/', views.index, name='portfolio'),
]