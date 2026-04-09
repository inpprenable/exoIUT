from lib import evaluate


def example_sort(arr: list[int]) -> list[int]:
    return sorted(arr)


# ===============================
# Execution
# ===============================

if __name__ == "__main__":
    for name, func in SOLUTIONS:
        evaluate(func, name)

def thomas_sort(arr: list[int]) -> list[int]:
    return sorted(arr)





SOLUTIONS = [
    ("example", example_sort),("thomas", thomas_sort)
]

