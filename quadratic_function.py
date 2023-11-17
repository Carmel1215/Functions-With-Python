import matplotlib.pyplot as plt
import numpy as np

from utility import *

def print_quadratic_function_menu():

    clear()
    print()
    print('=====================================================')
    print('이차함수 메뉴')
    print('=====================================================')
    print()
    print('[0] 뒤로가기')
    print('[1] 이차함수 식 구하기')
    print('[2] 이차함수 그리기')
    print()

def print_get_quadratic_equation_menu():
    
    clear()
    print()
    print('=====================================================')
    print('일차함수 식 구하기')
    print('=====================================================')
    print()

def get_quadratic_equation():
    pass

def print_quadratic_function():

    clear()
    print()
    print('=====================================================')
    print('이차함수 그리기')
    print('=====================================================')
    print()

    try:
        a = float(input('그리고자 하는 이차함수의 이차항의 계수를 입력해주세요 : '))
    except ValueError:
        wrong_input()

    clear()
    print()
    print('=====================================================')
    print('이차함수 그리기')
    print('=====================================================')
    print()

    try:
        b = float(input('그리고자 하는 이차함수의 일차항의 계수를 입력해주세요 : '))
    except ValueError:
        wrong_input()

    clear()
    print()
    print('=====================================================')
    print('이차함수 그리기')
    print('=====================================================')
    print()

    try:
        c = float(input('그리고자 하는 이차함수의 상수항을 입력해주세요 : '))
    except ValueError:
        wrong_input()

    # 그래프 출력
    x = np.arange(-40, 40, 0.01)

    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.axis((-20,20,-20,20))

    plt.grid(color = "gray", alpha=.5, linestyle='--')

    plt.plot(x, a*(x**2) + b*x + c)

    plt.show()