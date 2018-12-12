'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

from itertools import count

def main():
	s = input()
	# the input string is in s
	# remove pass and start your code here
	maxSubstr = s[0:0]
	for start in range(len(s)):
		for end in count(start + len(maxSubstr) + 1):
			substr = s[start:end]
			if len(substr) != (end - start):
				break
			if sorted(substr) == list(substr):
				maxSubstr = substr

	print("Longest substring in alphabetical order is: " + str(maxSubstr))


if __name__== "__main__":
	main()
