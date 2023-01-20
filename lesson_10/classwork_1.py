"""
Создать функцию при помощи регулярных выражений для проверки, что строка является валидным телефонным номером в формате
+375 (29) 299-29-29.
"""
import re


def main(phone_number):
    if re.fullmatch(r'^\+375\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$', phone_number):
        return 'yes'
    else:
        return 'no'

