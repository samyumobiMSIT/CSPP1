# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
	s = input()
	# epsilon and step are initialized
	# don't change these values
	x=25
	epsilon = 0.01
	step = 0.1
	# your code starts here
	numGuesses = 0
	ans = 0.0
	while abs(ans ** 2 - x) >= epsilon and ans <= x:
		ans += step
		numGuesses += 1
	print('numGuesses =', numGuesses)

	if abs(ans ** 2 - x) >= epsilon:
		print('Failed on square root of', x)

	else:
		print(ans, 'is close to square root of', x)

if __name__== "__main__":
	main()
