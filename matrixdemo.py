#Astro Ohnuma
#11/17/17
#matrixdemo.py - how to create/use a matrix

board = [['a','b','c'],['d','e','f'],['g','h','i']]

def printboard():
    for row in range(0,3):
        for col in range(0,3):
            print(board[row][col],' ',end = '')
        print()