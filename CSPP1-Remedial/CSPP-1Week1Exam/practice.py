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
    pass

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
