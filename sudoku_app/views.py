from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.http import JsonResponse

from . import forms
from .models import SudokuModel


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
        return render(
            request,
            self.template_name, {
                'page_title': self.page_title,
                'last_boards': q,
            }
        )


class sudoku_appIndexView(TemplateView):
    template_name = 'sudoku_app/base.html'


def index(request):
    return HttpResponse("hi there")
