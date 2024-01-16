#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Вывести «столбиком» его третий, шестой и т.д. символы.


if __name__ == '__main__':
    sentence = input("Введите предложение на русском языке: ")

    if len(sentence) < 3:
        print("Введите предложение длиной минимум 3 символа")
    else:
        for i in range(2, len(sentence), 3):
            print(sentence[i])
