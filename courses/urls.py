from django.urls import path, re_path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    #re_path(r'^(?P<pk>\d+)/$', views.details, name='details'),
    #re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
    #path('<int:pk>/', views.details, name='details'),
    path('<slug:slug>/', views.details, name='details'),
]