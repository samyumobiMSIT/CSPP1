#Assume s is a string of lower case characters.

#program to count the number of vowels in given string.

#Number of vowels: 5

def main():
    '''this is main funtion'''
    input_string = input()
    # the input string is in s
    # remove pass and start your code here
    count_vowels = 0
    for letter_string in input_string:
        if letter_string in 'aeiou':
            count_vowels += 1

    print(count_vowels)
	

if __name__== "__main__":
	main()
