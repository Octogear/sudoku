from django.conf.urls import url
from . import views

app_name = 'api_v1'

urlpatterns = [
    url('health', views.HealthView.as_view(), name='app_index'),
]
