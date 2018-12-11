"""Sudoku generator."""

# created by Kostya C. aka tevtonez 26.10.2018
# updated by Kostya C. aka tevtonez 08.12.2018

import random
import copy

del_cell = {
    '0': 20,
    '1': 42,
    '2': 49,
    '3': 56,
}


def _move_parts(l, field_l):
    """Move line parts and append to field list."""
    field_l.append(l)
    l_1 = l[3:] + l[:-6]
    l_2 = l_1[3:] + l_1[:-6]
    field_l.append(l_1)
    field_l.append(l_2)


def _remove_numbers(field_l, n):
    """Remove n numbers from the field."""
    while True:
        if n == 0:
            break
        line_n = random.randint(0, 8)
        position_n = random.randint(0, 8)
        if field_l[line_n][position_n] != 0:
            field_l[line_n][position_n] = 0
            n -= 1


# def _print_field(field):
#     """Print field."""
#     count_3lines = 0
#     print('|-------|-------|-------|')
#     for x in field:
#         c = 0
#         print('|', end=" ")
#         for i in x:
#             print(i, end=" ")
#             c += 1
#             end = ' '
#             if c >= 9:
#                 end = '\n'
#             if c % 3 == 0:
#                 print('|', end=end)
#         count_3lines += 1
#         if count_3lines % 3 == 0:
#             print('|-------|-------|-------|')


def gen_field(n):
    """Generate sudoku field."""
    field = []

    l1 = [x for x in range(1, 10)]
    random.shuffle(l1)
    _move_parts(l1, field)

    l2 = l1[1:] + l1[:1]
    _move_parts(l2, field)

    l3 = l2[1:] + l2[:1]
    _move_parts(l3, field)
    solution = copy.deepcopy(field)
    _remove_numbers(field, del_cell[n])

    return field, solution
