# 1. Write a Python program to get a string from a given string where all occurrences of its "r" char have been changed to '$'.
# example: 'restart'   Result : '$esta$t'
my_str = "Best Restorants in Yerevan"
l_my_str = my_str.lower() # for changing capital letters too
x = l_my_str.replace("r", "$")
print(x)



# 2. Write a Python program to swap comma and dot in a string. 
# Sample string: "32.054,23"  Expected Output: "32,054.23"
str_1 = "32.054,23"
maketrans = str_1.maketrans
str_1 = str_1.translate(maketrans(",.", ".,"))
print(str_1)





# 3. Write a Python program to compute sum of digits of a given string
txt = "The team consists of 3 boys and 5 girls"
x = 0
for i in txt:
	if i.isdigit():
		x += int(i)
print("There are",x,"people in the tem.")



# # 4. Write a Python program to remove spaces from a inputed sentence.
snt = input("Enter the message_ ")
print(snt.replace(" ", ""))



# 5. Write python program to print even length words from inputed sentence.
message = input("Enter yoyr text to count letters: ")
x = 0
for i in message:
	if i.isalpha():
		x += 1
print(x)



# 6. Write a program to count how many letters and numbers are in given word. Example: "2 + 2 is equal to 4"
txt = "2 + 2 is equal to 4"
x = 0
y = 0
for i in txt:
	if i.isdigit():
		x += 1
		# print("There are",x,"numbers in this text")
	if i.isalpha():
		y += 1
print("You have",y,"letters and",x,"numbers in your text")



# 7. Write a Python program to count the number of characters (character frequency) in a string.
#example:"hello world"    output: h 1  e 1  l 3  ...
txt = "hello world"
frq = {}
for i in txt:
	if i in frq:
		frq[i] += 1
	else:
		frq[i] = 1
print("{}".format(txt),str(frq))



# 8. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
inp = input("Please make your comment: ")
print(inp.upper())
print(inp.lower())



# # 9. Write a Python script that has a list and convert into comma separated string.
# #Sample list:['Geeks', 'for', 'Geeks']     output:Geeks-for-Geeks
lst = ['Geeks', 'for', 'Geeks']
new_str = "-".join(lst)
print(new_str)



# 10. Python program to convert  starting letter of a word in upper case format or in the title format.
#sample list: ["hello", "this", "is", "pythonlobby"]   output: Hello This Is Pythonlobby
s_list = ["hello", "this", "is", "pythonlobby"]
new_text = " ".join(s_list)
print(new_text.title())