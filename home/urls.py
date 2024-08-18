from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lock_dashboard/', views.lock_dashboard, name='lock_dashboard'),
    # path('geocode/', views.geocode_address, name='geocode_address'),
    path('send_message_to_esp32/', views.send_message_to_esp32, name='send_message_to_esp32'),
]
