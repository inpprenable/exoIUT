from lib import evaluate


def example_sort(arr: list[int]) -> list[int]:
    return sorted(arr)

# ===============================
# Execution
# ===============================

def thomas_sort(arr_t: list[int]) -> list[int]:
    return sorted(arr_t)

def fonction_idrys(arr: list[int]) -> list[int]:
    nouvelle_liste = []
    for nombre in arr:
        nouvelle_liste.append(nombre)
    taille = len(nouvelle_liste)
    for i in range(taille):
        for j in range(0, taille - i - 1):
            if nouvelle_liste[j] > nouvelle_liste[j + 1]:
                temp = nouvelle_liste[j]
                nouvelle_liste[j] = nouvelle_liste[j + 1]
                nouvelle_liste[j + 1] = temp
    return nouvelle_liste

def trie_mathieu(arr_m: list[int]) -> list[int]:
	return sorted(arr_m)

SOLUTIONS = [
    ("example", example_sort),("thomas", thomas_sort),("mathieu", trie_mathieu)
]


if __name__ == "__main__":
    for name, func in SOLUTIONS:
        evaluate(func, name)
