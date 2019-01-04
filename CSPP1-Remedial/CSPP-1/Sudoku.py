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
	for y in range(9):
		r = getRV(y,ls)
		c = getCV(y,ls)
		if len(set(r))!=len(r):
			raise Exception("duplicate")
		if len(set(c))!=len(c):
			raise Exception("duplicate")



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


def grid(j,i,ls):
	s = []
	t = False
	for srow in range(0,3):
		for scol in range(0, 3):
			if srow == j and scol == i:
				t = True
			s.append(ls[srow][scol])
	if t == True:
		return s
	s = []
	t = False
	for srow in range(0,3):
		for scol in range(3, 6):
			if srow == j and scol == i:
				t = True
			s.append(ls[srow][scol])
	if t == True:
		return s
	s = []
	t = False
	for srow in range(0,3):
		for scol in range(6, 9):
			if srow == j and scol == i:
				t = True
			s.append(ls[srow][scol])
	if t == True:
		return s
	s = []
	t = False
	for srow in range(3,6):
		for scol in range(0, 3):
			if srow == j and scol == i:
				t = True
			s.append(ls[srow][scol])
	if t == True:
		return s
	s = []
	t = False
	for srow in range(3,6):
		for scol in range(3, 6):
			if srow == j and scol == i:
				t = True
			s.append(ls[srow][scol])
	if t == True:
		return s
	s = []
	t = False
	for srow in range(3,6):
		for scol in range(6, 9):
			if srow == j and scol == i:
				t = True
			s.append(ls[srow][scol])
	if t == True:
		return s
	s = []
	t = False
	for srow in range(6,9):
		for scol in range(0, 3):
			if srow == j and scol == i:
				t = True
			s.append(ls[srow][scol])
	if t == True:
		return s
	s = []
	t = False
	for srow in range(6,9):
		for scol in range(3, 6):
			if srow == j and scol == i:
				t = True
			s.append(ls[srow][scol])
	if t == True:
		return s
	s = []
	t = False
	for srow in range(6,9):
		for scol in range(6, 9):
			if srow == j and scol == i:
				t = True
			s.append(ls[srow][scol])
	if t == True:
		return s


''' Possibile values in sudoku '''
def pv(ls):
	for j in range(len(ls)):
		# len= 9*9, a: data 
		for i in range(len(ls[0])):
			#loop moves from 0 till end
			if ls[j][i] == '.':
				r = getRV(j,ls)
				c = getCV(i,ls)
				gv = grid(j,i,ls)
				ans = r + c + gv
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






