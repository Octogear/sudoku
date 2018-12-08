from django.urls import path, re_path
from . import views

urlpatterns = [
    path('health/', views.HealthView.as_view(), name="check-health"),
    re_path('gen/', views.SudokuApiView.as_view(), name="generate"),
    re_path('last/', views.SudokuApiView.as_view(), name="generate"),
]
