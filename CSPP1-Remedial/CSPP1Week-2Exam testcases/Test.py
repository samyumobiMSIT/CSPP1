def sum_list(l):
    s=0
    for i in l:
        if isinstance(i,list):
          s += sum_list(i)
        else:
            try:
                s+=i
            except TypeError:
              continue
    return s

def count_list(l):
    if l is []:
        return l




def main():
    lst = eval(input())
    print(sum_list(lst))
    print(count_list(lst))


if __name__ == '__main__':
    main()


