from django.urls import path, re_path
from . import views

# router = routers.DefaultRouter()

urlpatterns = [
    # url(r'^', include(router.urls)),
    path('health/', views.HealthView.as_view(), name="check-health"),
    path('gen/', views.GenSudoku.as_view(), name="generate"),
    path('last/', views.ListSudoku.as_view(), name="generate"),
    re_path(r'^check(?P<id>\d*)$', views.CheckSudoku.as_view(), name="check-sudoku"),
]
