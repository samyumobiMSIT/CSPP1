#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	input_string = input()
	# the input string is in s
	# remove pass and start your code here
	count = 0
	for letter in s:
		if letter in 'aeiou':
			count +=1
	print('number of vowels: ' + str(count))
	

if __name__== "__main__":
	main()
