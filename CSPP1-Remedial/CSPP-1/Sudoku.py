"""
Length of sudoku should be 81 , no duplicate values in grid
if number is not inputed raise
"""
def ensure81(v):
	if len(v) != 81:
		raise Exception("Invalid input")
	elif '.' not in v:
		raise Exception("Given sudoku is solved")
'''
Values should be between 1 2 9 and 
should not have duplicate values in row or col
'''
def ensurenodup(ls):
	dup = list()
	for box in ls:
		if box!=".":
			if box not in dup:
				dup.append(box)
			else:
				raise Exception("duplicate")
				return


def getRV(j ,ls):
	r = []
	for y in ls[j]:
		if y!='.':
			r.append(y)
	return r

def getCV(j, ls):
	c = []
	#iterating all row values where value!='.'
	for r in ls:
         c.append(r[j])
	return c


def grid(j,i,ls ):

    s = list()
    if(j >= 0 & j < 9) & (i >=0 & i < 9):
        for srow in range(0,9): #subrow, subcol
            for scol in range(0,9):
                s.append(ls[srow][scol])
    return s

def data(box,j,ls):
	n = [1,2,3,4,5,6,7,8,9]
	new = []
	#get roe, col, grid values
	r_v = condatatoint(getRV(box,ls))
	c_v = condatatoint(getCV(box,ls))
	g_v = condatatoint(grid(box,j,ls))
	result = ""
	for box in n:
		if box not in r_v and c_v and g_v:
			new.append(box)
	result = ''.join(list(map(str,new)))
	print(result)

def condatatoint(integer) :
	r = ''.join(integer)
	r = r.replace(".","")
	r = list(r)
	mapped = list(map(int,r))
	return mapped


''' Possibile values in sudoku '''
def pv(ls):

	for j in range(len(ls)):
		# len= 9*9, a: data 
		for i in range(len(ls[0])):
			#loop moves from 0 till end
			if ls[j][i] == '.':
				r = getRV(j,ls)
				c = getCV(i,ls)
				ans = r + c +
				space = ' '
				for x in range(1,10):
					#checking if data is btw 1 2 9 and is = ans
					if str(x) not in ans:
						space = space + str(x)
					print(space)

'''
Main Function
'''
def main() :
	v1 = input()
	v = list(v1)
	k = 0
	ls =[]
	try:
		ensure81(v1)
		while(k < 81):
			r = []
			for l in range(9):
				r.append(v[l])
				l = l + 1
			ls.append(r)
		ensurenodup(ls)
		pv(ls)
	except Exception as f:
		print(f)


if __name__ == '__main__':
	main()






