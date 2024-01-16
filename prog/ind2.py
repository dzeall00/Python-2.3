#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Дано предложение. Определить, есть ли в нем буквосочетания чу или щу. В случае
# положительного ответа найти также порядковый номер первой буквы первого из них.


if __name__ == '__main__':
    sentence = input("Введите предложение: ").lower()

position_chu = sentence.find('чу')
position_shu = sentence.find('щу')

if position_chu != -1 and (position_chu < position_shu or position_shu == -1):
    print(f"Буквосочетание 'чу' найдено в позиции: {position_chu + 1}")

elif position_shu != -1 and (position_shu < position_chu or position_chu == -1):
    print(f"Буквосочетание 'щу' найдено в позиции: {position_shu + 1}")

else:
    print("Буквосочетание 'чу' и 'щу' не найдено.")
