import math
import matplotlib.pyplot as plt
import numpy as np

from utility import *

def print_floor_function_menu():

    clear()
    print()
    print('=====================================================')
    print('가우스 함수 메뉴')
    print('=====================================================')
    print()
    print('[0] 뒤로가기')
    print('[1] 가우스 함수 그리기')
    print()

def print_floor_function():

    clear()
    print()
    print('=====================================================')
    print('가우스 함수 그리기')
    print('=====================================================')
    print()

    
    x = np.arange(-4.0, 4.0, 0.1)
    y = []

    for i in range(len(x)):
        y.append(math.floor(x[i]))

    # 그래프 출력
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.axis((-4, 4, -4, 4))

    plt.grid(color = "gray", alpha=.5, linestyle='--')

    plt.plot(x, y, '.')

    plt.show()