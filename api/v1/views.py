"""Api endpoints."""
from django.contrib import messages
from django.views.generic import View
from django.http import JsonResponse

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from django.http import Http404

from django.shortcuts import get_object_or_404


import sudoku_app.models as sudoku_models
from .serializers import SudokuModelSerializer, CheckSudokuSerializer

from .script_sudoku import gen_field


class GenSudoku(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """POST allowed. Creates a board.Takes param 'board_diffic' from 0 to 3."""

    queryset = sudoku_models.SudokuModel.objects.all().order_by('-id')[:25]
    serializer_class = SudokuModelSerializer

    def post(self, request, *args, **kwargs):
        """POST method."""
        board, solution = gen_field(request.data['board_diffic'][0])

        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['board_data'] = str(board)
        request.POST['board_solution'] = str(solution)
        request.POST._mutable = mutable
        return self.create(request, *args, **kwargs)


class ListSudoku(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    """GET allowed. Displays 25 last sudoku."""

    queryset = sudoku_models.SudokuModel.objects.all().order_by('-id')[:25]
    serializer_class = SudokuModelSerializer

    def get(self, request, *args, **kwargs):
        """GET method."""
        return self.list(request, *args, **kwargs)


class CheckSudoku(APIView):
    """Check sudoku solution."""

    def get_object(self, id):
        """Search for the object."""
        try:
            return sudoku_models.SudokuModel.objects.get(pk=id)
        except sudoku_models.SudokuModel.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        """GET method."""
        id = int(request.query_params.get('id'))
        obj = self.get_object(id)
        serializer = CheckSudokuSerializer(obj)
        return Response(serializer.data)


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
