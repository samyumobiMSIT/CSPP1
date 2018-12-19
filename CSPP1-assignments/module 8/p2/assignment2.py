def sum_of_digits(input_num):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if input_num == 0:
        return 0
    return input_num % 10 + sum_of_digits(input_num // 10)


def main():
    '''main function'''
    input_num = input()
    print(sum_of_digits(int(input_num)))
if __name__ == "__main__":
    main()
