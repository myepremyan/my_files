# 1. Write a Python program to reverse a string.
# Sample String : "1234abcd"     Expected Output : "dcba4321"
def rev_function(str):
	return str[::-1]
print(rev_function("1234abcd"))


# 2. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
# Sample Items : green-red-yellow-black-white     Expected Result : black-green-red-white-yellow
my_words = input("Enter words: ")
def sort_function(str):
	lst = sorted(str.split("-"))
	new_str = "-".join(lst)
	return new_str
new_str = sort_function(my_words)
print(new_str)


# 3. Write a Python program to print the floating numbers up to 2 decimal places
def my_function(float):
	return "{:.2f}".format(float)
print(my_function(3.1465))


# 4.Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,then tell them whether they guessed too low, too high, or exactly right.
import random
guessed_num = int(input('Guess a number from 1 to 10: '))
def random_function(rand_num):
	global guessed_num
	while rand_num != guessed_num:
		if guessed_num > rand_num:
			guessed_num = int(input("Too high, print next one: ")) 
		elif guessed_num < rand_num:
			guessed_num = int(input("Too low, print next one: "))	
	else:
		print("Exactly right!")
random_function(random.randint(1,10))


# 5. Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# num = int(input("Enter a number: "))
def divisors_function(num):
	for i in range(1, num + 1):
		if(num % i == 0):
			print(i)
divisors_function(int(input("Enter a number: ")))
