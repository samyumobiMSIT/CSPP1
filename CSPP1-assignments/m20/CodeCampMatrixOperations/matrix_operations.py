'''matrix operations'''
from operator import add
def mult_matrix(matrix1_dimension, matrix_1, matrix2_dimension, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if matrix1_dimension[0] != matrix2_dimension[1] or matrix1_dimension[1] != matrix2_dimension[0]:
        print("Error: Matrix shapes invalid for mult")
        return None
    multi_matrix = []
    for i in range(matrix1_dimension[0]):
        row_list = []
        for j in range(matrix1_dimension[0]):
            ele_ment = 0
            for k in range(matrix1_dimension[1]):
                ele_ment += matrix_1[i][k]*matrix_2[k][j]
               # print(matrix1[i][k], " ",matrix2[k][j])
            #print(h)
            row_list.append(ele_ment)
            #print(row)
        multi_matrix.append(row_list)
    return multi_matrix

def add_matrix(matrix1_dimension, matrix_1, matrix2_dimension, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if matrix1_dimension != matrix2_dimension:
        print("Error: Matrix shapes invalid for addition")
        return None
    sum_matrix = []
    for i in range(matrix1_dimension[0]):
        row_list = list(map(add, matrix_1[i], matrix_2[i]))
        sum_matrix.append(row_list)
    return sum_matrix
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    pass

def main():
    '''in main'''
    # read matrix 1

    # read matrix 2

    # add matrix 1 and mqtrix 2

    # multiply matrix 1 and matrix 2
    matrix1_dimension = input().split(",")
    matrix1_dimension = list(map(int, matrix1_dimension))
    matrix_1 = []
    for i in range(int(matrix1_dimension[0])):
        in_1 = input().split()
        in_1 = list(map(int, in_1))
        matrix_1.append(in_1)

    matrix2_dimension = input().split(",")
    matrix2_dimension = list(map(int, matrix2_dimension))
    matrix_2 = []
    for i in range(int(matrix2_dimension[0])):
        in_2 = input().split()
        in_2 = list(map(int, in_2))
        matrix_2.append(in_2)

    error_msg = ""
    len_row = len(matrix_1[0])
    #print(len_row)
    for i in matrix_1:
        #print(i, "i")
        if len(i) != len_row:
            error_msg = "Error: Invalid input for the matrix"
    len_row = len(matrix_2[0])
    #print(len_row)
    for i in matrix_2:
        #print(i, "i")
        if len(i) != len_row:
            error_msg = "Error: Invalid input for the matrix"
    if error_msg == "":
        print(add_matrix(matrix1_dimension, matrix_1, matrix2_dimension, matrix_2))
        print(mult_matrix(matrix1_dimension, matrix_1, matrix2_dimension, matrix_2))
    else:
        print(error_msg)


if __name__ == '__main__':
    main()
