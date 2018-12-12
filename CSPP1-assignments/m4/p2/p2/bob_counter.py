'''Assume s is a string of lower case characters.

program to print the number of times the string 'bob' occurs in s

Number of times bob occurs is: 2'''

def main():
    s = input()
    countBob = 0
    for i in range(len(s)):
        if s[i:].startswith('bob'):
            countBob += 1
    print(str(countBob))

if __name__ == "__main__":
    main()
