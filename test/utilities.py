from time import sleep
from colorama import Fore, Style


# Ширина рамки
width_init = 80

color_list = [
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, 
]

def border():
    for i in range(width_init):
        print('*', end='')
    else:
        print()


def line(text=''):
    if len(text) <= width_init:
        if text == '':
            for i in range(width_init):
                if i == 0 or i+1 == width_init:
                    print('*', end='')
                else:
                    print(' ', end='')
            else:
                print()
        else:
            len_text = len(text)
            index_start = int((width_init - len_text) / 2)
            pos = 0
            for i in range(width_init):
                if i == 0 or i+1 == width_init:
                    print('*', end='')
                elif i == index_start:
                    pos = 0
                    print(text[pos], end='')
                elif i > index_start and pos + 1 < len_text:
                    pos += 1
                    print(text[pos], end='')
                else:
                    print(' ', end='')
            else:
                print()
    else:
        print('ERROR! Ошибка при выводе строки.')


def phase(index:int, text:str) -> None:

    print(color_list[index%len(color_list)])
    border()
    line()
    line(f'Фаза {index}')
    line()
    line(text)
    line()
    border()
    print(Style.RESET_ALL)

