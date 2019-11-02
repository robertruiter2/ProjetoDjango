from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastre_se/', views.register, name='register'),
]