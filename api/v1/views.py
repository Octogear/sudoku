"""Api endpoints."""
from django.contrib import messages
from django.views.generic import View
from django.http import JsonResponse

from rest_framework import generics
import sudoku_app.models as sudoku_models
from .serializers import SudokuModelSerializer


class ListSudokuView(generics.ListAPIView):
    """Displays 25 last sudoku."""

    queryset = sudoku_models.SudokuModel.objects.all().order_by('-id')[:25]
    serializer_class = SudokuModelSerializer


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
