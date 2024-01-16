#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Даны два слова. Определить, можно ли из букв первого из них получить второе.
# Рассмотреть два варианта:
# повторяющиеся буквы второго слова могут в первом слове не повторяться;
# каждая буква второго слова должна входить в первое слово столько же раз, сколько и во второе.


def can_spell(word1, word2):
    # Проверка, что каждая буква из второго слова встречается в первом слове не более раза
    counts1 = {char: word1.count(char) for char in set(word1)}
    counts2 = {char: word2.count(char) for char in set(word2)}
    
    for char in counts2:
        if char not in counts1 or counts1[char] < counts2[char]:
            return False

    return True

def letter_repeat(word1, word2):
    # Проверка, что можно составить второе слово из первого без учета повторений букв
    for char in word2:
        if char not in word1:
            return False
    return True

if __name__ == '__main__':
    word1 = input("Введите первое слово: ").lower()
    word2 = input("Введите второе слово: ").lower()

    if can_spell(word1, word2):
        print(f"Можно составить слово '{word2}' из букв слова '{word1}'")
    else:
        print(f"Нельзя составить слово '{word2}' из букв слова '{word1}'")

    if letter_repeat(word1, word2):
        print(f"Можно составить слово '{word2}' из букв слова '{word1}' без учета повторяющихся букв")
    else:
        print(f"Нельзя составить слово '{word2}' из букв слова '{word1}' без учета повторяющихся букв")
