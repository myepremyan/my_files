#1. Write a Python program that takes two lists and returns True if they have at least one common member.
# list_1 = [1,4,6,7]
# list_2 = [3,10,5,9]
# result = "False"
# for i in list_1:
# 	for j in list_2:
# 		if i == j:
# 			result = "True"
# print(result)

			

#2. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
# colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# colors.pop(0)
# colors.pop(-1)
# colors.pop(-1)
# print(colors)



#3. Write a Python program to get the difference between the two lists
# fruits_a = ['apple', 'banana', 'orange', 'apricot']
# fruits_b = ['avocado', 'mango', 'apple', 'apricot']
# diff = []
# for i in fruits_a:
# 	if i not in fruits_b:
# 		diff.append(i)
# for j in fruits_b:
# 	if j not in fruits_a:
# 		diff.append(j)
# print(diff)



# #4.  Write a Python program to find the second smallest number in a list.
# numbers = [7,12,26,8,14,5,33]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers[1])



#5. Getting the first three items of a list
# cities = ['London', 'Paris', 'Lisbon', 'Madrid']
# print(cities[0:3])



#6. Write a Python program to remove duplicates from a list.
# month = [4, 10, 10, 6, 11, 6]
# unique_month = []
# for x in month:
# 	if x not in unique_month:
# 		unique_month.append(x)
# print(unique_month)