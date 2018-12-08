"""Serializers."""
from rest_framework import serializers
from sudoku_app.models import SudokuModel


class SudokuModelSerializer(serializers.ModelSerializer):
    """Sudoku board serializer."""

    class Meta:
        model = SudokuModel
        fields = ("id", "board_title", "board_data", "board_solution", "board_diffic")

        def create(self, validated_data):
            instance = SudokuModel.objects.create(**validated_data)

            return instance
