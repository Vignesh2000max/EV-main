from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('charge/',views.charge, name='charge'),
    path('<str:st_name>/', views.bookSlot, name='bookSlot'),
    path('', views.home, name='usershome'),
]
