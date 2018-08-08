#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(L, f):
    for i in range(len(L)):
        L[i]=f(L[i])

L=[1,-2,3.33]
apply_to_each(L,abs)
print(L)

def main():
    data = input()
    data = data.split()
    list1 = []
    #for j in l:
        #list1.append(int(j))
    apply_to_each(list1, abs)
    print ('listl',list1)

if __name__ == "__main__":
    main()
