''' Write a python program to find if the given number is a perfect cube or not
using guess and check algorithm '''

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    '''main function'''
    # input is captured in ssquare_num
    square_num = int(input())
    # watch out for the data type of value stored in s
    # your code starts here
    sq_flag = 0
    for guess_num in range(square_num):
        if guess_num*guess_num*guess_num == square_num:
            sq_flag = 1
            break
    if sq_flag == 1:
        print(str(square_num)+" is a perfect cube")
    else:
        print(str(square_num)+" is not a perfect cube")



if __name__ == "__main__":
    main()
