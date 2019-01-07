def img(f):
    i = f.split('<img')
    e_t = "\""
    i=i[1:]
    c = 0
    t = "src = \""
    s = []
    for item_1 in i:
        if "src=\"" in item_1:
            #s +=item_1
            index = item_1.index(t)
            item_1=item_1[index+len(t):]
            end = item_1.index(e_t)
            c +=1
            #print all the URLs of the image
            print(item_1[:end])
            s.append(item_1)
    print(c)
#Display the count of images present on the webpage

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
        if "!" not in j:
            j = j[1:].replace(" ", "")
            end.append(j)
            c +=1
    for q in end:
        index = q.index("}")
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



def ls(f):
    l = f.split("</li>")
    tag = "li"
    midtag = "<"
    end = ">"
    c = 0
    s = []
    for item in l:
        if "<li>" in item:
            # s +=item_1
            index = item.index(tag)
            item_1 = item[index + len(tag):]
            end = item.index(end)
            c += 1
            # print all the URLs of the image
            print(str(item[:end]))
            s.append(item)
        print(c)




def main():
    f = open("webpage5.html",encoding="utf8").read()
    #print(f.encode("utf-8"))
    #inputs option for either image background or list
    o = input()
    if o == 'image':
        img(f)
    elif o == 'background':
        bg(f)
    elif o == 'list':
        ls(f)


# Do the default


if __name__ == '__main__':
    main()
