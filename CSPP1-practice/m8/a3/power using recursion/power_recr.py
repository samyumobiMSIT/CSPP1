# Exercise: PowerRecr
# Write a Python function, recurPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    count = exp - 1

    # Debug print statement, remove before submitting
    print('Result: ' + str(result) + ' Base: ' + str(base))
    while count >= 0:
        # Multiply result by itself
        result *= base

        # Debug print statement, remove before submitting
        print(str(result))

        # Reduce the value of exp
        count -= 1

    return result

def main():
    data = input()
    data = data.split()
    print(str(recurPower(float(data[0]),int(data[1]))))

if __name__== "__main__":
    main()