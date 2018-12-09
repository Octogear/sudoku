"""Main models."""
from django.db import models
from .utils.auxiliary import gen_unique

from django.db.models.signals import post_save
from django.dispatch import receiver


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
    board_data = models.CharField(
        null=True,
        blank=True,
        max_length=423
    )
    board_solution = models.CharField(
        null=True,
        blank=True,
        max_length=261
    )


class CounterModel(models.Model):
    """Counter."""

    count = models.IntegerField(
        default=0,
    )

    def __str__(self):
        """String repr."""
        return "Generated boards: {}".format(self.count)


@receiver(post_save, sender=SudokuModel)
def update_counter(sender, instance, **kwargs):
    """Update counter every time a board is generated."""
    q = CounterModel.objects.all()
    if len(q) != 1:
        obj = CounterModel.objects.create()
    else:
        obj = CounterModel.objects.all()[0]
    obj.count += 1
    obj.save()
