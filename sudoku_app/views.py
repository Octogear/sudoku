from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.http import JsonResponse

from . import forms
from .models import SudokuModel, CounterModel


class SignUpView(CreateView):
    """Signup view."""

    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'sudoku_app/signup.html'


class IndexView(TemplateView):
    """Index view."""

    template_name = 'index.html'
    page_title = "Generate Sudoku"

    def get(self, request, *args, **kwargs):
        """Get method."""
        q = SudokuModel.objects.all().order_by('-id')[:4]  # .filter()
        count = CounterModel.objects.all()[0].count
        return render(
            request,
            self.template_name, {
                'page_title': self.page_title,
                'last_boards': q,
                'count': count,
                'base_url': "{0}://{1}{2}".format(request.scheme, request.get_host(), request.path),
            }
        )


class ApiView(TemplateView):
    """Index view."""

    template_name = 'sudokuapi.html'
    page_title = "Sudoku Generator API v.1"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name, {
                'base_url': "{0}://{1}{2}".format(request.scheme, request.get_host(), request.path),
            }
        )

class sudoku_appIndexView(TemplateView):
    template_name = 'sudoku_app/base.html'


def index(request):
    return HttpResponse("hi there")
