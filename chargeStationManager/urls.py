from django.urls import path
from . import views

app_name='manager'

urlpatterns = [
    path('home/',views.home, name='managerHome'),
    path('manage_slots/',views.manage_slots, name='manage_slots'),
    path('delete_slot/',views.delete_slot, name='delete_slot'),
]
