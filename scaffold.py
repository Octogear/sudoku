import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sudoku.settings")
django.setup()

from sudoku_app.models import SudokuModel

def create_ten():
    """Generate 10 sudoku boards."""
    for i in range(10):
        SudokuModel.objects.create(
            board_data="[[5, ' ', 7, 9, 4, 6, 2, ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 5, 8, ' '], [' ', ' ', 1, 5, 8, ' ', 9, 4, ' '], [' ', ' ', 9, ' ', 6, 2, 3, ' ', ' '], [4, 6, 2, ' ', 1, ' ', ' ', 7, 9], [' ', 1, 5, ' ', 7, 9, ' ', ' ', 2], [7, ' ', ' ', ' ', 2, ' ', ' ', 5, 8], [6, ' ', ' ', ' ', ' ', 8, ' ', 9, ' '], [1, 5, 8, 7, ' ', 4, 6, 2, 3]]",
            board_solution="[[5, 8, 7, 9, 4, 6, 2, 3, 1], [9, 4, 6, 2, 3, 1, 5, 8, 7], [2, 3, 1, 5, 8, 7, 9, 4, 6], [8, 7, 9, 4, 6, 2, 3, 1, 5], [4, 6, 2, 3, 1, 5, 8, 7, 9], [3, 1, 5, 8, 7, 9, 4, 6, 2], [7, 9, 4, 6, 2, 3, 1, 5, 8], [6, 2, 3, 1, 5, 8, 7, 9, 4], [1, 5, 8, 7, 9, 4, 6, 2, 3]]",
        )


if __name__ == "__main__":
    create_ten()
