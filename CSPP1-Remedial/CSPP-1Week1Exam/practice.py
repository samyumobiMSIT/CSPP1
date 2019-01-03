def img(f):
    i = f.split('><')
    tag = "img src = "
    end_tag = " data-"
    c=0
    s = []
    for item_1 in i:
        if "img src=\ " '' in item_1 and " data- " in item_1:
            s +=item_1
            index = item_1.index(tag)
            item_1=item_1[index+len(tag):]
            end = item_1.index(end_tag)
            c +=1


def bg(f):

    final = ";"
    initial = ":"
    bg_color= f.split(";")
    t = "background-color"
    ans=[]
    for data in bg_color:
        if t in data:
            #s is background[0]
            index=data.index(t)
            data = data[index +len(t) : ]
            ans.append(data)

    #Display the colours in sorted order (remove duplicate colours)
    srt = list(ans)
    c = 0
    end = []
    for j in srt:
        for q in end:
            index=q.index("}")
            q = q[:index]
            print(index)
            end.append(q)
    end_res=sorted(end)
    print(end_res)
    #Display the count of different colours present on the webpage
    for y in end_res:
        if "}" not in y:
            print(y)
    print(c)



    # for c in ans:
    #     if ":" in c:
    #         s=c.s(initial)
    #         c = c[s +len(initial) : ]
    #         print(c)
    # set_c =set(end)



def ls(f):
    pass



def main():
    f = open("webpage5.html",encoding="utf8").read()
    print(f.encode("utf-8"))
    #inputs option for either image background or list
    o = input()
    if o == 'img':
        img(f)
    elif o == 'bg':
        bg(f)
    elif o == 'ls':
        ls(f)




# Do the default


if __name__ == '__main__':
    main()
