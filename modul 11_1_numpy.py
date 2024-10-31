import numpy as np
import pandas as pd

# Доступна индексация
a = np.array([10, 20, 30, 40])
b = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(f"a[0] = {a[0]}")
print(f"b[0] = {b[0]}")

# Доступны стандартные арифмитические действия
a = np.array([9, 8, 7])
b = np.array([1, 2, 3])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Обращение к отдельному элементу в двумерном массиве
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a[0, 4])

# Операторы min и max находят минимальное и максимальное значение.
a = np.array([[1, 2, 3], [4, 5, 6]])
min_all = a.min()
max_all = a.max()
print(min_all)
print(max_all)