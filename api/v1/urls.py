from django.urls import path, re_path
from . import views


urlpatterns = [
    path('health/', views.HealthView.as_view(), name="check-health"),
    # re_path('gen/(?P<difficulty>)/', views.GenSudokuView.as_view(), name="generate"),
    re_path('last/', views.ListSudokuView.as_view(), name="generate"),
]
