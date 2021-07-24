# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 12:48:38 2021

@author: Sadi Mohammad
"""

global N
N = 4


def printSolution(board) :
    for i in range(N) :
        for j in range(N) :
            print(board [ i ] [ j ], end=" ")
        print()


def isSafe(board, row, col) :
    for i in range(col) :
        if board [ row ] [ i ] == 1 :
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)) :
        if board [ i ] [ j ] == 1 :
            return False

    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)) :
        if board [ i ] [ j ] == 1 :
            return False

    return True


def solveNQUtil(board, col) :
    if col >= N :
        return True

    for i in range(N) :

        if isSafe(board, i, col) :

            board [ i ] [ col ] = 1

            if solveNQUtil(board, col + 1) == True :
                return True

            board [ i ] [ col ] = 0

    return False
    # if solveNQUtil(board, 0) == False :
    #     print("Error Solution.......")
    #     return False
    # printSolution(board)
    # return True


def solveNQ() :
    board = [ [ 0, 0, 0, 0 ],
              [ 0, 0, 0, 0 ],
              [ 0, 0, 0, 0 ],
              [ 0, 0, 0, 0 ] ]

    if solveNQUtil(board, 0) == False :
        print("Error Solution.......")
        return False

    printSolution(board)
    return True


solveNQ()