# Exercise: Is In
# Write a Python function, isIn(j, aStr), that takes in two arguments a character and String and returns the isIn(j, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(j, aStr):
    '''
    j: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    low = 0
    high = len(aStr)
    mid = (low + high) / 2

    i = 0

    # Set limits on how many times loop will run
    while i < 50:
        i += 1
        # If string is empty return False
        if len(aStr) <= 0:
            return False
        # if  j = middle character return True
        if j == aStr[mid]:
            return True
        # if we've gone through entire string and not found match
        # return False
        if (low == mid or high == mid) and (j != aStr[mid]):
            return False
        else:
            # if j is greater than the midpoint, move selection
            # of string up
            if j > aStr[mid]:
                low = mid
                return isIn(j, aStr[low:high])
            # if j is greater than the midpoint, move selection
            # of string down
            else:
                high = mid
                return isIn(j, aStr[low:high])
   

def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))


if __name__== "__main__":
    main()