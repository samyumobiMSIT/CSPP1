def factorial(input_num):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if input_num in (0, 1):
        return 1
    return input_num * factorial(input_num - 1)
def main():
    '''in main function'''
    input_num = input()
    print(factorial(int(input_num)))

if __name__ == "__main__":
    main()
