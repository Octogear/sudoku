"""Api endpoints."""
from django.contrib import messages
from django.views.generic import View
from django.http import JsonResponse

from rest_framework import generics
from rest_framework import mixins

import sudoku_app.models as sudoku_models
from .serializers import SudokuModelSerializer

from .script_sudoku import gen_field


class SudokuApiView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    : get - Displays 25 last sudoku.
    : post - Creates a board. Takes param 'board_diffic' from 0 to 3.
    """

    queryset = sudoku_models.SudokuModel.objects.all().order_by('-id')[:25]
    serializer_class = SudokuModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("\nHERE")
        print(gen_field(request.data['board_diffic'][0]))
        print("HERE\n")
        board, solution = gen_field(request.data['board_diffic'][0])

        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['board_data'] = str(board)
        request.POST['board_solution'] = str(solution)
        request.POST._mutable = mutable

        return self.create(request, *args, **kwargs)


class SudokuCreateView(generics.ListAPIView):
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
