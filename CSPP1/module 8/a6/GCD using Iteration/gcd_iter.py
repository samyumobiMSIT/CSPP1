# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor = 0

    # Test to see which variable is smaller
    if a < b:
        divisor = a
    elif a > b:
        divisor = b
    else:
        divisor = a

    while divisor > 1:
        if a % divisor == 0:
            if b % divisor == 0:
                return divisor
        divisor -= 1
    return 1


def main():
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1])))
    #print(" gcdIter(2, 12): " + str(gcdIter(2, 12)))
    #print(" gcdIter(6, 12): " + str(gcdIter(6, 12)))


if __name__== "__main__":
    main()