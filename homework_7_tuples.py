# 1.Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
#example:tuple1 = (11, [22, 33], 44, 55)   output:tuple1 = (11, [222, 33], 44, 55)
# my_tuple = (11, [22, 33], 44, 55)
# my_list = list(my_tuple)
# my_list[1] = [222, 33]
# print(tuple(my_list))



# 2.Write a Python program convert a given string list to a tuple.  Original string: python 3.0
# Convert the said string to a tuple:   ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
# languge_name = "python 3.0"
# new_tuple = tuple(languge_name)
# print(new_tuple)



# 3.Check if all items in the tuple are the same
# cities = ('Madrid', 'Madrid', 'Madrid')
# cities_list = list(cities)
# checklist = []
# for i in cities_list:
# 	if i not in checklist:
# 		checklist.append(i)
# if len(checklist) > 1:
# 	print('You have different items in your tuple')
# else:
# 	print('All items in your tuple are the same')



# 4.Get the maximum and minimum values for set without max() and min() and without cast to list.
# given_set = {1,5,12,21,36,55}
# max_value = given_set.pop()
# min_value = max_value
# for i in given_set:
# 	if i > max_value:
# 		max_value = i
# for j in given_set:
# 	if j < min_value:
# 		min_value = j
# print(f"The max is {max_value} and min is {min_value}")


# given_list = [1,5,12,21,36,-10,55]
# min_value = given_list[0]
# for j in given_list:
# 	if j < min_value:
# 		min_value = j
# print(f"min is {min_value}")
		
		


# 5. Write a Python program to check if two given sets have no elements in common.
# set_1 = {11, 26, 34, 40}
# set_2 = {60, 15, 32, 18, 22}
# result = True
# for i in set_1: 
# 	for j in set_2:
# 		if i == j:
# 		 result = False
# print(result)



# 6.Write a Python program to convert a tuple to a string.
# given_tuple = ('P', 'y', 't', 'h', 'o','n')
# best_language = "".join(given_tuple)
# print(best_language)



# 7.Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:  (('333', '33'), ('1416', '55'))
# New tuple values:  ((333, 33), (1416, 55))
original_tup = (('333', '33'), ('1416', '55'))
for i in original_tup:
	new_tup = (int(i[0])), (int(i[1]))
	print(tuple(new_tup),end = '')



# my_set = set()
# # print(type(my_set))
# my_set.add(5)
# my_set.update({3,2,6,10})
# my_set.pop()
# print(my_set)


# set_1 = {11, 23, 46, 40}
# set_2 = {23, 10, 40, 16, 25}
# print(set_1.difference(set_2), set_2.difference(set_1))
# print(set_1.difference_update(set_2))



# l1 = [1,4,5]
# l2 = [1,5,6,7]
# l3 = [10,5,7]
# print(set(l1).intersection(l2).intersection(l3))


