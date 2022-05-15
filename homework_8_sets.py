# 1.Write a program (using functions!) that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order. 
txt = input("Type the text: ")
txt_list = txt.split()
txt_list.reverse()
back_txt = " ".join(txt_list)
print(back_txt)


# 2.You, the user, will have in your head a number between 0 and 100.
 #The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
import random
x = random.randint(1,100)
y = int(input('Guess a number from 1 to 100: '))
while x != y:
	if y > x:
		y = int(input("Too high, print next one: ")) 
	elif y < x:
		y = int(input("Too low, print next one: "))	
else:
	print("Congrats, you find the number!")



# 3. Take two lists, and write a program that returns a list that without duplicates. Use list comprehension!
lst_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst_2 = [0, 2, 0, 4, 5, 11, 8, 21, 21]
new_lst = []
[new_lst.append(i) for i in lst_1 if i not in new_lst]
[new_lst.append(j) for j in lst_2 if j not in new_lst]
print(new_lst)


# 4.Write a Python program to return a new set with unique items from both sets by removing duplicates.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_set = set1.union(set2)  # version_1
# unique_set = set1 | set2       # version_2
print(unique_set)


# 5.Remove items from set1 that are not common to both set1 and set2
set_1 = {10, 20, 30, 40, 50}
set_2 = {30, 40, 50, 60, 70}
new_set = {i for i in set_1 if i in set_2}
print(new_set)


# 6.input a text and add vowels in set .
txt = input("Enter the text: ")
my_set = set()
for i in txt:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
		my_set.update(i)
print(my_set)
