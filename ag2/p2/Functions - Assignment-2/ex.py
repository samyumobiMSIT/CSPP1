i=0

while i<5:
    c = 0
    for letter in "hello, world":
        c +=1
        if i % 2 == 0:
            break
        print("i"+ str(i) + "; count is: " + str(c))
        i +=1