from lib import evaluate


def example_sort(arr: list[int]) -> list[int]:
    return sorted(arr)

# ===============================
# Execution
# ===============================

def thomas_sort(arr_t: list[int]) -> list[int]:
    return sorted(arr_t)

def trie_mathieu(arr_m: list[int]) -> list[int]:
	return sorted(arr_m)

SOLUTIONS = [
    ("example", example_sort),("thomas", thomas_sort),("mathieu", trie_mathieu)
]


if __name__ == "__main__":
    for name, func in SOLUTIONS:
        evaluate(func, name)

