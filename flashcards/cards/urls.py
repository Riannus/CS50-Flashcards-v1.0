from django.urls import path
from . import views

urlpatterns = [
    path('cards/', views.cards, name='cards'),
]