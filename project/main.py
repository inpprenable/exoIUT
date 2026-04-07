from lib import evaluate


def example_sort(arr: list[int]) -> list[int]:
    return sorted(arr)


SOLUTIONS = [
    ("example", example_sort),
]

# ===============================
# Execution
# ===============================

if __name__ == "__main__":
    for name, func in SOLUTIONS:
        evaluate(func, name)
