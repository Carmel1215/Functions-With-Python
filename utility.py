import os
import math

def clear():
    os.system('cls')

def pause():
    os.system('pause')

def wrong_input():
    clear()
    print()
    print('잘못된 입력입니다. 다시 입력해주세요.')
    print()
    pause()

def delete_point(num) -> int:
    del_num = num

    if math.floor(num) == num:
        del_num = math.floor(num)

    return del_num

def add_sign(num) -> str:
    num = delete_point(num)

    if num >= 0:
        num = str('+ {0}'.format(num))
        return num
    elif num < 0:
        num = str('- {0}'.format(num))
        return num