#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Eсли в кортеже есть хотя бы одна тройка соседних чисел, 
# в которой средний элемент больше своих «соседей», 
# т. е. предшествующего и последующего, то напечатать все элементы, 
# предшествующие элементам последней из таких троек.

import sys

if __name__ == "__main__":
        input_tuple = tuple(map(int, input("Введите минимум 3 элемента кортежа через пробел: ").split()))
        if len(input_tuple) < 3:
            print("Ошибка: необходимо ввести минимум 3 элемента", file=sys.stderr)
            exit(1)

        found_triplet = False
        for i in range(len(input_tuple) - 2):
            if input_tuple[i] < input_tuple[i+1] > input_tuple[i+2]:
                result = input_tuple[:i] if i > 0 else input_tuple[:i+1]
                print("Предшествующие элементы: ", result)
                found = True
                break

        if not found:
            print("Нет тройки соседних чисел, в которой средний элемент больше своих «соседей»")
