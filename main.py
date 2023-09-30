# import
import os
import math
import matplotlib.pyplot as plt
import numpy as np

# 메인 메소드
def Main():
    # 프로그램 종료용 변수
    is_exit = True

    clear()
    print_banner()
    pause()

    # 메인 루프
    while is_exit:
        print_menu()

        try:
            main_user_input = int(input('무엇을 하시겠습니까? : '))
        except ValueError:
            wrong_input()
            continue


        if main_user_input == 0: # 프로그램 종료
            is_exit = False

        elif main_user_input == 1: # 일차함수

            while 1:
                print_linear_function_menu()
            
                try:
                    linear_user_input = int(input('무엇을 하시겠습니까? : '))
                except ValueError:
                    wrong_input()

                if linear_user_input == 0:
                    break
                elif linear_user_input == 1:
                    get_linear_equation()
                elif linear_user_input == 2:
                    print_linear_function()
                else:
                    wrong_input()

        elif main_user_input == 2: # 이차함수

            while 1:
                print_quadratic_function_menu()

                try:
                    quadratic_user_input = int(input('무엇을 하시겠습니까? : '))
                except ValueError:
                    wrong_input()

                if quadratic_user_input == 0:
                    break
                elif quadratic_user_input == 1:
                    print_quadratic_function()
                else:
                    wrong_input()

        elif main_user_input == 3: # 가우스 함수
            
            while 1:
                print_floor_function_menu()

                try:
                    floor_user_input = int(input('무엇을 하시곘습니까? : '))
                except ValueError:
                    wrong_input()

                if floor_user_input == 0:
                    break
                elif floor_user_input == 1:
                    print_floor_function()
                else:
                    wrong_input()

        else:
            wrong_input()

# 일차함수 관련 메소드
def print_linear_function_menu():

    clear()
    print('')
    print('=====================================================')
    print('일차함수 메뉴')
    print('=====================================================')
    print('')
    print('[0] 뒤로가기')
    print('[1] 일차함수 식 구하기')
    print('[2] 일차함수 그리기')
    print('')

def print_get_linear_equation_menu():
    
    clear()
    print('')
    print('=====================================================')
    print('일차함수 식 구하기')
    print('=====================================================')
    print('')

def get_linear_equation():
    
    print_get_linear_equation_menu()

    try:
        first_x = float(input('첫 번째 점의 X 좌표를 입력해주세요 : '))
    except ValueError:
        wrong_input()

    print_get_linear_equation_menu()

    try:
        first_y = float(input('첫 번째 점의 Y 좌표를 입력해주세요 : '))
    except ValueError:
        wrong_input()

    print_get_linear_equation_menu()

    try:
        second_x = float(input('두 번째 점의 X 좌표를 입력해주세요 : '))
    except ValueError:
        wrong_input()

    print_get_linear_equation_menu()

    try:
        second_y = float(input('두 번째 점의 Y 좌표를 입력해주세요 : '))
    except ValueError:
        wrong_input()
        
    a = (first_y - second_y) / (first_x - second_x)
    b = first_y - (a * first_x)

    print_get_linear_equation_menu()

    print('일차함수의 식은 : ' + 'y = {0}x {1}'.format(delete_point(a), add_sign(b)))
    print('')
    pause()

def print_linear_function():
    
    clear()
    print('')
    print('=====================================================')
    print('일차함수 그리기')
    print('=====================================================')
    print('')

    try:
        a = float(input('그리고자 하는 일차함수의 기울기를 입력해주세요 : '))
    except ValueError:
        wrong_input()

    clear()
    print('')
    print('=====================================================')
    print('일차함수 그리기')
    print('=====================================================')
    print('')

    try:
        b = float(input('그리고자 하는 일차함수의 Y절편을 입력해주세요 : '))
    except ValueError:
        wrong_input()

    # 그래프 출력
    x = np.array(range(-15,16))

    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.axis((-10,10,-10,10))

    plt.grid(color = "gray", alpha=.5, linestyle='--')

    plt.plot(x, a*x + b)

    plt.show()

# 이차함수 관련 메소드
def print_quadratic_function_menu():

    clear()
    print('')
    print('=====================================================')
    print('이차함수 메뉴')
    print('=====================================================')
    print('')
    print('[0] 뒤로가기')
    print('[1] 이차함수 그리기')
    print('')

def print_quadratic_function():
    pass

# 가우스 함수 메소드
def print_floor_function_menu():

    clear()
    print('')
    print('=====================================================')
    print('가우스 함수 메뉴')
    print('=====================================================')
    print('')
    print('[0] 뒤로가기')
    print('[1] 가우스 함수 그리기')
    print('')

def print_floor_function():

    clear()
    print('')
    print('=====================================================')
    print('가우스 함수 그리기')
    print('=====================================================')
    print('')

    
    x = np.arange(-3.0, 3.1, 0.1)
    y = []

    for i in range(len(x)):
        y.append(math.floor(x[i]))

    # 그래프 출력
    
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.axis((-3,3,-3,3))

    plt.grid(color = "gray", alpha=.5, linestyle='--')

    plt.plot(x, y, '.')

    plt.show()

# 출력 메소드
def print_banner():
    txt = '''
=====================================================
파이썬으로 함수 표현하기
=====================================================

v1.0.0
Made by TaeHwan
'''
    print(txt)

def print_menu():
    
    clear()
    print('')
    print('=====================================================')
    print('메인 메뉴')
    print('=====================================================')
    print('')
    print('[0] 프로그램 종료')
    print('[1] 일차함수')
    print('[2] 이차함수')
    print('[3] 가우스 함수')
    print('')

# 편의성 메소드
def clear():
    os.system('cls')

def pause():
    os.system('pause')

def wrong_input():
    clear()
    print('')
    print('잘못된 입력입니다. 다시 입력해주세요.')
    print('')
    pause()

def delete_point(num):
    del_num = num

    if math.floor(num) == num:
        del_num = math.floor(num)

    return del_num

def add_sign(num):
    num = delete_point(num)

    if num >= 0:
        num = str('+ {0}'.format(num))
        return num
    elif num < 0:
        num = str('- {0}'.format(num))
        return num

Main() # Run Main Method