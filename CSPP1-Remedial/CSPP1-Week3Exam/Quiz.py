def declarequiz(list1,list2):
    #store values in list of list
    #list2 = {}
    total = 0
    #a = input().split("|")
    # quesno = input(a[1])
    # response = input(a[2])
    # answer = input(a[3])
    # points = int((input(a[4])))
    for i in list1:
        for j in list2:
            #Check whether the response is equal to the answer or not.
            if i == j:
                #Total score = ( No. of points student got/Total number of points ) * 100
                total = int(list1[i]/list2[j]*100)
                #print(total)
                if total < 0:
                    total = 0
                print(i + ": " + str(float(total)) + "%")

def main():
   noflines = int(input())
   list1 = {}
   list2 = {}
   try:
       for i in range(noflines):
           a = input().split("|")
           if a[0] not in list1:
               list1[a[0]] = 0
               list2[a[0]] = int(a[4])
           else:
               list2[a[0]] += int(a[4])
           if a[2] == a[3]:
                list1[a[0]] += int(a[4])
           else:
               list1[a[0]] -= int(a[4])

       declarequiz(list1,list2)

   except ValueError:
       print("Invalid Points")






if __name__ == '__main__':
    main()