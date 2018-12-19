#define the simple_divide function here
def simple_divide(item, denom):
    # start a try-except block
    try:
    	div = item/denom
    	return div
    except ZeroDivisionError:
    	return 0
   
def fancy_divide(list_of_numbers, index):
	div_li = []
	for i in list_of_numbers:
		div_li.append(simple_divide(i,index))
	return div_li
    

def main():
	data = input()
	l=data.split()
	l1=[]
	for j in l:
		l1.append(float(j))
	s=input()
	index=int(s)
	print(fancy_divide(l1,index))
	

if __name__== "__main__":
	main()
