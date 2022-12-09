from django.urls import path
# django tiene un tempalte preparado para le login
# Es decir no provee de la clase LoginView para poder mostrar el formalario de inicio de session
from django.contrib.auth.views import LoginView, logout_then_login
from .views import RegisterView

# Segun el documento de django la url correact para que funcion debe ser accounts/login/
urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_then_login, name='logout'),
]