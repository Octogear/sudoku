import os
import django

from django_cron import CronJobBase, Schedule
from .models import SudokuModel


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sudoku_app.settings")
django.setup()


class ClearBoards(CronJobBase):
    RUN_EVERY_MINS = 1400

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        """Main cron method."""
        q = SudokuModel.objects.all().order_by('-board_c_time')[25:]

        for board in q:
            board.delete()
