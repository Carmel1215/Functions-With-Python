# import
from utility import *
from linear_function import *
from quadratic_function import *
from floor_function import *

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
                    continue

                if linear_user_input == 0:
                    linear_user_input = None
                    break
                elif linear_user_input == 1:
                    linear_user_input = None
                    get_linear_equation()
                elif linear_user_input == 2:
                    linear_user_input = None
                    print_linear_function()
                else:
                    linear_user_input = None
                    wrong_input()
                    continue

        elif main_user_input == 2: # 이차함수

            while 1:
                print_quadratic_function_menu()

                try:
                    quadratic_user_input = int(input('무엇을 하시겠습니까? : '))
                except ValueError:
                    wrong_input()
                    continue

                if quadratic_user_input == 0:
                    quadratic_user_input = None
                    break
                elif quadratic_user_input == 1:
                    quadratic_user_input = None
                    print_quadratic_function()
                elif quadratic_user_input == 2:
                    quadratic_user_input = None
                    get_quadratic_equation()
                else:
                    quadratic_user_input = None
                    wrong_input()
                    continue

        elif main_user_input == 3: # 가우스 함수
            
            while 1:
                print_floor_function_menu()

                try:
                    floor_user_input = int(input('무엇을 하시겠습니까? : '))
                except ValueError:
                    wrong_input()
                    continue

                if floor_user_input == 0:
                    floor_user_input = None
                    break
                elif floor_user_input == 1:
                    floor_user_input = None
                    print_floor_function()
                else:
                    floor_user_input = None
                    wrong_input()
                    continue

        else:
            wrong_input()
            main_user_input = None

# 출력 메소드
def print_banner():
    txt = '''
=====================================================
파이썬으로 함수 표현하기
=====================================================

v1.2.1
Made by TaeHwan
'''
    print(txt)

def print_menu():
    
    clear()
    print()
    print('=====================================================')
    print('메인 메뉴')
    print('=====================================================')
    print()
    print('[0] 프로그램 종료')
    print('[1] 일차함수')
    print('[2] 이차함수')
    print('[3] 가우스 함수')
    print()

Main() # Run Main Method