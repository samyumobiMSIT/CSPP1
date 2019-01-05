'''count levels'''
def levels(l):
    ls = " "
    c = 0
    #additional list to capture [
    ls = ''.join(str(p) for p in l)
    for j in range(len(ls)):
        if ls[j] == '[':
            c += 1
    return c

'''count sum'''
def sum_list(l):
    s=0
    for i in l:
        #check if i is there in list and calc sum
        if isinstance(i,list):
          s += sum_list(i)
        else:
            try:
                s+=i
                '''except typeerrors'''
            except TypeError:
              continue
    return s

'''main'''
def main():
    lst = eval(input())
    print(sum_list(lst))
    print(levels(lst))

'''cmd'''
if __name__ == '__main__':
    main()


