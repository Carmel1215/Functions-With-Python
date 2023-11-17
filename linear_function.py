import matplotlib.pyplot as plt
import numpy as np

from utility import *

def print_linear_function_menu():

    clear()
    print()
    print('=====================================================')
    print('일차함수 메뉴')
    print('=====================================================')
    print()
    print('[0] 뒤로가기')
    print('[1] 일차함수 식 구하기')
    print('[2] 일차함수 그리기')
    print()

def print_get_linear_equation_menu():
    
    clear()
    print()
    print('=====================================================')
    print('일차함수 식 구하기')
    print('=====================================================')
    print()

def get_linear_equation():
    
    print_get_linear_equation_menu()

    try:
        first_x = float(input('첫 번째 점의 X 좌표를 입력해주세요 : '))
    except ValueError:
        wrong_input()
        get_linear_equation()

    print_get_linear_equation_menu()

    try:
        first_y = float(input('첫 번째 점의 Y 좌표를 입력해주세요 : '))
    except ValueError:
        wrong_input()
        get_linear_equation()

    print_get_linear_equation_menu()

    try:
        second_x = float(input('두 번째 점의 X 좌표를 입력해주세요 : '))
    except ValueError:
        wrong_input()
        get_linear_equation()

    print_get_linear_equation_menu()

    try:
        second_y = float(input('두 번째 점의 Y 좌표를 입력해주세요 : '))
    except ValueError:
        wrong_input()
        get_linear_equation()
        
    a = (first_y - second_y) / (first_x - second_x)
    b = first_y - (a * first_x)

    print_get_linear_equation_menu()

    print('일차함수의 식은 : ' + 'y = {0}x {1}'.format(delete_point(a), add_sign(b)))
    print()
    pause()

def print_linear_function():
    
    clear()
    print()
    print('=====================================================')
    print('일차함수 그리기')
    print('=====================================================')
    print()

    try:
        a = float(input('그리고자 하는 일차함수의 일차항의 계수를 입력해주세요 : '))
    except ValueError:
        wrong_input()
        print_linear_function()

    clear()
    print()
    print('=====================================================')
    print('일차함수 그리기')
    print('=====================================================')
    print()

    try:
        b = float(input('그리고자 하는 일차함수의 상수항을 입력해주세요 : '))
    except ValueError:
        wrong_input()
        print_linear_function()

    # 그래프 출력
    x = np.arange(-40, 40, 0.01)

    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.axis((-20,20,-20,20))

    plt.grid(color = "gray", alpha=.5, linestyle='--')

    plt.plot(x, a*x + b)

    plt.show()