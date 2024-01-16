#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Дано слово, оканчивающее символом «.».
# Составить программу, которая вставляет некоторую заданную букву после буквы с заданным номером.


import sys


if __name__ == '__main__':
    word = input("Введите слово, оканчивающееся символом '.':\n")
    
    if not word.endswith('.'):
        print("Ошибка: Входное слово не оканчивается символом '.'!",
              file=sys.stderr)
        exit(1)

    position = int(input("Введите номер буквы, после которой нужно вставить букву: "))
    if position <= 0 or position > len(word):
        print("Некорректная позиция", file=sys.stderr)
        exit(1)
    else:
        letter = input("Введите букву для вставки: ")
    # Вставляем заданную букву после буквы с заданным номером
    new_word = word[:position] + letter + word[position:]

    print("Результат:", new_word)
    exit(1)
