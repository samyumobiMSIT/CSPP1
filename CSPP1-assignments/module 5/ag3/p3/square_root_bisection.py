# Write a python program to find the square root of the given number
# using approsimation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''main function'''
    square_num = int(input())
    # epsilon and step are initialized
    # don't change these values
    approximation_val = 0.01
    # your code starts here
    high_val = square_num
    low_val = 0
    middle_val = (low_val + high_val) / 2

    while abs((middle_val ** 2) - square_num) >= approximation_val:
        if square_num > middle_val ** 2:
            low_val = middle_val
        else:
            high_val = middle_val
        middle_val = (low_val + high_val) / 2
    print(middle_val)

if __name__ == "__main__":
    main()

