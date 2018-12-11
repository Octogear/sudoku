from django.contrib import admin
from .models import SudokuModel, CounterModel


class AdminSudokuModel(admin.ModelAdmin):
    # list_display = [field.name for field in SudokuModel._meta.get_fields()]
    list_display = ['board_title', 'board_diffic', 'board_c_time', ]

admin.site.register(SudokuModel, AdminSudokuModel)
admin.site.register(CounterModel)
