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

def levels(l):
    s = " "
    c=0
    k = ''.join(str(p) for p in l)
    for j in range(len(l)):
        if s[j] == '[':
            c+=1
    return c






def main():
    lst = eval(input())
    print(sum_list(lst))
    print(levels(lst))


if __name__ == '__main__':
    main()


