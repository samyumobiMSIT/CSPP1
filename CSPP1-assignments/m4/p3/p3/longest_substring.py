'''Assume s is a string of lower case characters.
program that prints the longest substring of s in which the letters occur in alphabetical order.
'''
#longest string in alphabetical order

def main():
    '''this is main function'''
    in_strs = input()
    # the input string is in s
    # remove pass and start your code here
    count_1 = 0
    count_max = 0
    end_index = 0
    for index_strs in range(len(in_strs)-1):
        if ord(in_strs[index_strs]) <= ord(in_strs[index_strs+1]):
            count_1 += 1
        else:
            count_1 = 0
        if count_max < count_1:
            count_max = count_1
            end_index = index_strs + 1
    print(in_strs[end_index - count_max : end_index + 1])

if __name__ == "__main__":
    main()

