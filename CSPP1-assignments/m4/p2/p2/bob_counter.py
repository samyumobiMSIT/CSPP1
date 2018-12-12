'''Assume s is a string of lower case characters.

program to print the number of times the string 'bob' occurs in s

Number of times bob occurs is: 2'''

def main():
    s_s = input()
    count_Bob = 0
    for i in range(len(s_s)):
        if s_s[i:].startswith('bob'):
            count_Bob += 1
    print(str(count_Bob))

if __name__ == "__main__":
    main()
