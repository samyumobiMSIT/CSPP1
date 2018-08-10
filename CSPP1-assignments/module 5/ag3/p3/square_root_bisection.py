# Write a python program to find the square root of the given number
# using approsimation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
	s = 25
	# epsilon and step are initialized
	# don't change these values
	epsilon = 0.01
	step = 0.1
	# your code starts here
	numGuesses = 0
	low = 0.0
	high = max(1.0, s)
	ans = (high + low) / 2.0
	while abs(ans ** 2 - s) >= epsilon:
		numGuesses += 1
		if ans ** 2 < s:
			low = ans
		else:
			high = ans
		ans = (high + low) / 2.0
	print('numGuesses =', numGuesses)
	print(ans, 'is close to square root of', s)


if __name__== "__main__":
	main()

