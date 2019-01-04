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
	for y in range(0, 9):
		rv = getRV(y,ls)

		if len(set(rv))!=len(rv):
			raise Exception("Invalid Sudoku:Duplicate values")
		cv = getCV(y, ls)
		if len(set(cv))!=len(cv):
			raise Exception("Invalid Sudoku:Duplicate values")



def getRV(c1 ,ls):
	r = []
	for y in ls[c1]:
		if y!='.':
			r.append(y)

	return r

def getCV(c1, ls):
	c = []
	#iterating all row values where value!='.'
	for r in ls:
		if r[c1]!='.':
			c.append(r[c1])

	return c


def grid(l1,m1,ls):
	sg = []
	v1 = False
	for n1 in range(0,3):
		for p1 in range(0, 3):
			if n1 == l1 and p1 == m1:
				v1 = True
			sg.append(ls[n1][p1])
	if v1 == True:
	    return sg

	sg = []
	v1 = False
	for n1 in range(0, 3):
		for p1 in range(3, 6):
			if n1 == l1 and p1 == m1:
				v1 = True
			sg.append(ls[n1][p1])
	if v1 == True:
		return sg

	sg = []
	v1 = False
	for n1 in range(0, 3):
		for p1 in range(6, 9):
			if n1 == l1 and p1 == m1:
				v1 = True
			sg.append(ls[n1][p1])
	if v1 == True:
		return sg

	sg = []
	v1 = False
	for n1 in range(3, 6):
		for p1 in range(0, 3):
			if n1 == l1 and p1 == m1:
				v1 = True
			sg.append(ls[n1][p1])
	if v1 == True:
		return sg

	sg = []
	v1 = False
	for n1 in range(3, 6):
		for p1 in range(3, 6):
			if n1 == l1 and p1 == m1:
				v1 = True
			sg.append(ls[n1][p1])
	if v1 == True:
		return sg

	sg = []
	v1 = False
	for n1 in range(3, 6):
		for p1 in range(6, 9):
			if n1 == l1 and p1 == m1:
				v1 = True
			sg.append(ls[n1][p1])
	if v1 == True:
		return sg

	sg = []
	v1 = False
	for n1 in range(6, 9):
		for p1 in range(0, 3):
			if n1 == l1 and p1 == m1:
				v1 = True
			sg.append(ls[n1][p1])
	if v1 == True:
		return sg

	sg = []
	v1 = False
	for n1 in range(6, 9):
		for p1 in range(3, 6):
			if n1 == l1 and p1 == m1:
				v1 = True
			sg.append(ls[n1][p1])
	if v1 == True:
		return sg

	sg = []
	v1 = False
	for n1 in range(6, 9):
		for p1 in range(6, 9):
			if n1 == l1 and p1 == m1:
				v1 = True
			sg.append(ls[n1][p1])
	if v1 == True:
		return sg


''' Possibile values in sudoku '''
def pv(ls):
	for n1 in range(len(ls)):
		# len= 9*9, a: data 
		for p1 in range(len(ls[0])):
			#loop moves from 0 till end
			if ls[n1][p1] == '.':
				rvl = getRV(n1,ls)
				cvl = getCV(p1,ls)
				gv = grid(n1,p1,ls)
				ans = rvl + cvl + gv
				space = ' '
				for l1 in range(1,10):
					#checking if data is btw 1 2 9 and is = ans
					if str(l1) not in ans:
						space += str(l1)
					print(space)

'''
Main Function
'''
def main() :
	v1 = input()
	v = list(v1)
	n1 = 0
	ls =[]
	try:
		ensure81(v1)
		while(n1 < 81):
			r = []
			for k in range(0, 9):
				r.append(v[n1])
				n1 = n1 + 1
			ls.append(r)
		ensurenodup(ls)
		pv(ls)
	except Exception as f:
		print(f)


if __name__ == '__main__':
	main()






