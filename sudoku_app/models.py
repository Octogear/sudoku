"""Main models."""
from django.db import models
from .utils.auxiliary import gen_unique


class SudokuModel(models.Model):
    """Sudoku board class."""

    class Meta:
        verbose_name = "SudokuModel"
        verbose_name_plural = "SudokuModels"

    def __str__(self):
        """String repr."""
        return "{}".format(self.board_title)

    def save(self, *args, **kwargs):
        """Owerriding save method to create board title."""
        self.board_title = gen_unique()
        super(SudokuModel, self).save(*args, **kwargs)

    board_title = models.CharField(
        max_length=12,
        null=False,
        blank=False,
        editable=False,
    )
    board_c_time = models.DateTimeField(
        'Created Time',
        auto_now_add=True,
        null=True,
    )
    board_diffic = models.CharField(
        default='0',
        max_length=1,
        null=False,
        blank=False
    )
