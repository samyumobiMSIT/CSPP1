'''Assume s is a string of lower case characters.

program to print the number of times the string 'bob' occurs in s

Number of times bob occurs is: 2'''
def main():
    '''This is main function'''
    s_s = input()
    count_bob= 0
    for i in range(len(s_s)):
        if s_s[i:].startswith('bob'):
            count_bob+= 1
    print(str(count_bob))

if __name__ == "__main__":
    main()
