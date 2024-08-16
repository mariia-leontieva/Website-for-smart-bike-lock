from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lock_dashboard/', views.lock_dashboard, name='lock_dashboard'),
]
