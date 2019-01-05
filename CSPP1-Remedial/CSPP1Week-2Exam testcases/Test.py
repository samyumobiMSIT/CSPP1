def sum_list(l):
    sum=0
    for i in l:
        if isinstance(i,list):
            sum = sum + sum_list(i)
        else:
            sum = sum + i
    print(sum)

def main():
    sum_list(lst)


if __name__ == '__main__':

    lst = input()
    main()

