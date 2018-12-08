"""Creating 10 sudoku boards."""

import requests
import random


def create_ten():
    """Generate 10 sudoku boards."""
    difficulty = ['0', '1', '2', '3']
    for i in range(10):
        dif_val = random.choice(difficulty)
        print(dif_val)
        requests.post(
            "http://127.0.0.1:8000/api/v1/gen/",
            data={'board_diffic': dif_val}
        )


if __name__ == "__main__":
    create_ten()
