from morse_dict import *


def letters_to_morse(letters: str) -> str:
    morse_str = ''
    for char in letters:
        if char.upper() in l_to_m:
            morse_str += l_to_m[char.upper()] + ' '
    if len(morse_str) != 0:
        return morse_str
    else:
        return 'Вы ввели не верные символы'


def rus_l_to_morse(letters: str) -> str:
    morse_str = ''
    for char in letters:
        if char.lower() in rus_to_m:
            morse_str += rus_to_m[char.lower()] + ' '
    if len(morse_str) != 0:
        return morse_str
    else:
        return 'Вы ввели не верные символы'


def morse_to_letters(morse: str) -> str:
    letters_str = ''
    morse_list = morse.split()
    for char in morse_list:
        if char in m_to_l:
            letters_str += m_to_l[char] + ' '
    if len(letters_str) != 0:
        return letters_str
    else:
        return 'Вы ввели неверные символы'


def morse_to_rus_l(morse: str) -> str:
    letters_str = ''
    morse_list = morse.split()
    for char in morse_list:
        if char in m_to_rus:
            letters_str += m_to_rus[char] + ' '
    if len(letters_str) != 0:
        return letters_str
    else:
        return 'Вы ввели неверные символы'
