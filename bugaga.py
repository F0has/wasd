def sieve_eratosthenes(start, end):
    if end < 2:
        return []
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(end ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, end + 1, i):
                is_prime[j] = False
    return [num for num in range(max(start, 2), end + 1) if is_prime[num]]

import random

def shuffle_words(text):
    words = text.split()
    random.shuffle(words)
    return ' '.join(words)

def zero_column(matrix, col_index):
    for row in matrix:
        if col_index < len(row):
            row[col_index] = 0
    return matrix

matrix = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55],
]
zero_column(matrix, 2)
print(matrix)