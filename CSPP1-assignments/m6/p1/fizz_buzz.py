'''print fizz for 3 multiples
#print buzz for 5 multiples
#print fizz and buzz for 5 multiples'''

def main():
    '''
    Read number from the input, store it in variable num.
    '''
    input_num = int(input())
    start_index = 1
    while start_index <= input_num:
        if start_index % 3 == 0 or start_index % 5 == 0:
            if start_index % 3 == 0:
                print("Fizz")
            if start_index % 5 == 0:
                print("Buzz")
        else:
            print(start_index)

        start_index += 1

if __name__ == "__main__":
    main()
