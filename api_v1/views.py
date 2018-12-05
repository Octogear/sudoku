from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.http import JsonResponse

from . import models

# Create your views here.


class HealthView(View):
    """Health view."""

    def get(self, request, *args, **kwargs):
        """Get method."""
        from django.db import connections
        from django.db.utils import OperationalError
        db_conn = connections['default']
        try:
            db_conn.cursor()
        except OperationalError:
            connected = False
            response = '400'
        else:
            connected = True
            response = '200'
        data = {
            'response': response,
            'db_connected': connected,
        }
        return JsonResponse(data)
