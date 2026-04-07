# sort_challenge.py

import random
import time


# ===============================
# Instrumentation
# ===============================

class Counter:
    def __init__(self):
        self.comparisons = 0
        self.writes = 0


class CountedInt:
    def __init__(self, value, counter):
        self.value = value
        self.counter = counter

    def __lt__(self, other):
        self.counter.comparisons += 1
        return self.value < other.value

    def __le__(self, other):
        self.counter.comparisons += 1
        return self.value <= other.value

    def __gt__(self, other):
        self.counter.comparisons += 1
        return self.value > other.value

    def __ge__(self, other):
        self.counter.comparisons += 1
        return self.value >= other.value

    def __eq__(self, other):
        self.counter.comparisons += 1
        return self.value == other.value

    def __repr__(self):
        return str(self.value)


def wrap_array(arr, counter):
    return [CountedInt(x, counter) for x in arr]


def unwrap_array(arr):
    return [x.value for x in arr]


# ===============================
# Génération de tests
# ===============================

def generate_tests() -> list[list[int]]:
    tests = []

    # petits cas
    for _ in range(5):
        tests.append([random.randint(0, 50) for _ in range(10)])

    # moyens
    for _ in range(5):
        tests.append([random.randint(0, 1000) for _ in range(100)])

    # pire cas (déjà trié inversé)
    tests.append(list(range(200, 0, -1)))

    # doublons
    tests.append([random.randint(0, 5) for _ in range(200)])

    return tests


TESTS: list[list[int]] = generate_tests()


# ===============================
# Evaluation
# ===============================

def evaluate(func, name):
    total_score = 0
    total_time = 0
    total_comp = 0

    for arr in TESTS:
        counter = Counter()
        counted = wrap_array(arr, counter)

        start = time.perf_counter()
        result = func(counted.copy())
        elapsed = time.perf_counter() - start

        result = unwrap_array(result)

        if result == sorted(arr):
            total_score += 1

        total_time += elapsed
        total_comp += counter.comparisons

    print(f"{name:10} | score={total_score}/{len(TESTS)} | time={total_time:.6f}s | comps={total_comp}")
