"""App routing"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContinentsView.as_view(), name='root'),
    path('continent/<int:pk>', views.ContinentView.as_view(), name='continent'),
    path('continents/', views.ContinentsView.as_view(), name='continens'),
]
