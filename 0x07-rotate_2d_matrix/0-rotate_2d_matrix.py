#!/usr/bin/python3
''' Rotate 2D Matrix
'''


def rotate_2d_matrix(matrix):
    ''' Rotate 2D Matrix by 90 degree
    '''
    left, right = 0, len(matrix) - 1

    while (left < right):
        for i in range(right - left):
            top, bottom = left, right

            # save the first value then pivot
            topLeft = matrix[top][left + i]

            # pivot all items except the first one
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]

            # fill the last value with the first one
            matrix[top + i][right] = topLeft
        right = right - 1
        left = left + 1
