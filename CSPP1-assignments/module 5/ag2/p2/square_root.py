# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''This is main function'''
    square_num = int(input())
    aprroximation_val = 0.01
    step_val = 0.1
    guess_num = 0.0

    while guess_num <= square_num:
        if abs(guess_num**2 -square_num) < aprroximation_val:
            break
        else:
            guess_num += step_val

    if abs(guess_num**2 - square_num) >= aprroximation_val:
        print('fail')
    else:
        print(str(guess_num))

if __name__ == "__main__":
    main()
