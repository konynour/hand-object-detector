import pyfirmata
import numpy as np

comport ='COM10'

pin = np.array([2,3,4,5,6,7,8,9])
digit = np.array([[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[0,0,0,0,0,0,0]])
board=pyfirmata.Arduino(comport)
def led(fingers1):

    if fingers1==[1, 0, 0, 0, 0]:
        i = 0
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[6][j])
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[i][j])
    elif fingers1==[1, 1, 0, 0, 0]:
        i = 1
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[6][j])
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[i][j])
    elif fingers1==[1, 1, 1, 0, 0]:
        i = 2
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[6][j])
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[i][j])
    elif fingers1==[1, 1, 1, 1, 0]:
        i = 3
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[6][j])
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[i][j])
    elif fingers1==[1, 1, 1, 1, 1]:
        i = 4
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[6][j])
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[i][j])
    elif fingers1==[0, 1, 1, 1, 1]:
        i=5
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[6][j])
        for j in range(0, 7):
            board.digital[pin[j]].write(digit[i][j])





