import numpy as np
import time

def jadval_shift(array, table_array):
    array_shifted = np.zeros(table_array.shape[0], dtype='int')
    for index, value in enumerate(table_array): array_shifted[index] = array[value - 1]
    return array_shifted

def qator_split(array):
    left_split = array[:int(len(array) / 2)]
    right_split = array[int(len(array) / 2):]
    return left_split, right_split

def Shift_LtoR(array):
    temp = array[0]
    for index in range(1, len(array)): array[index - 1] = array[index]
    array[len(array) - 1] = temp
    return array

table_p_10 = np.array([3, 5, 2, 7, 4, 10, 1, 9, 8, 6,3,5])
table_p_08 = np.array([6, 3, 7, 4, 8, 5, 10, 9])

inputKey = input("12 bitli kalitni kiriting:")
key = list(inputKey)

def split_and_merge(key):
    left_split, right_split = qator_split(key)
    return np.concatenate((Shift_LtoR(left_split), Shift_LtoR(right_split)))

def key_generation_1(key, table):
    k = jadval_shift(key, table)
    key_merge = split_and_merge(k)
    return jadval_shift(key_merge, table)

def key_generation_2(key, table): return split_and_merge(key)

key_1 = key_generation_1(key, table_p_10)
print("".join([str(elem) for elem in key_1]))

key_2 = key_generation_2(key_1, table_p_08)
print("".join([str(elem) for elem in key_2]))

time.sleep(30)