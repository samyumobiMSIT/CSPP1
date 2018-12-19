# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.
def is_found(low_val, high_val, char, sorted_str):
    middle_val = (low_val+high_val)//2
    #print(middle_val)
    
    if sorted_str[middle_val] == char:
        return "True"
    elif middle_val == low_val or middle_val == high_val:
        return "False"
    else:
        if sorted_str[middle_val] < char:
            return is_found(middle_val, high_val, char, sorted_str)
        elif sorted_str[middle_val] > char:
            return is_found(low_val, middle_val, char, sorted_str)
        

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    sorted_str = sorted(aStr)
    sorted_str = ''.join(sorted_str)
    #print(sorted_str)
    low_val = 0
    high_val = len(sorted_str)
    x = is_found(low_val, high_val, char, sorted_str)
    return x

       

def main():
    char_input = input()
    string_input = input()
    if char_input == "" or string_input == "":
        print("no input given")
    else:
        print(isIn(char_input, string_input))


if __name__== "__main__":
    main()