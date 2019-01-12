def declarequiz(list1,list2):
    list2 = {}
    total = 0
    a = input().split("|")
    # quesno = input(a[1])
    # response = input(a[2])
    # answer = input(a[3])
    # points = int((input(a[4])))
    for i in list1:
        for j in list2:
            #Check whether the response is equal to the answer or not.
            if i == j:
                #Total score = ( No. of points student got/Total number of points ) * 100
                total = (int(list[i]) / int(list[j])) * 100
                #print(total)
                print(i + ":" + str(float(total)+"%"))

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

       # quesno = input(a[1])
       # response = input(a[2])
       # answer = input(a[3])
       # points = int((input(a[4])))
   #print(list1)

       #response == answer then points count
       if a[2] == a[3]:
           list1[a[0]] += int(a[4])
       else:
           list1[a[0]] -= int(a[4])
   # deduct points if not equal
   #invalid points
   except ValueError:
       print("Error")

   declarequiz(list1,list2)

if __name__ == '__main__':
    main()