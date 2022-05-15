# 1.Use the sorted() function to sort the list in ascending order with lambda.
my_lst = ['orange', 'banana', 'apple', 'avocado', 'peach']
sorted_lst = sorted(my_lst, key = lambda x: x[0])
print(sorted_lst)


# 2. Write a Python program to sort each sublist of strings in a given list of lists using lambda.
# Original list using lambda: [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
first_list = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
sorted_list = [sorted(i, key = lambda x: x[0]) for i in first_list]
print(sorted_list)


# 3.Write a Python program to count float number in a given mixed list using lambda.
Original_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
new_list = list(filter(lambda x: isinstance(x, float), Original_list))
print(len(new_list))


# 4. Write a Python program to count the occurrences of the items in a given list using lambda. Go to the editor
# Original list:[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Count the occurrences of the items in the said list:  {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}
lst_1 = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
new_dict = dict(map(lambda x: (x, list(lst_1).count(x)), lst_1))
print(new_dict)


# 5.Write a Python program to remove None value from a given list using lambda function.
# Original list: [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list: [12, 0, 23, -55, 234, 89, 0, 6, -12]
first_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
filtered_list = list(filter(lambda x: x is not None, first_list))
print(filtered_list)


# 6. Write a Python program to check whether a given string is number or not using Lambda.
# Sample Output: True  True  False  True
my_func = lambda a: True if a.isnumeric() else False
print(my_func('5'))
print(my_func('15'))
print(my_func('Fruit'))


# 7. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
# Original arrays: [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:  [2, 5, 7, 8, 9, -10, -3, -1]
lst_1 = [-1, 2, -3, 5, 7, 8, 9, -10]
my_func = lambda lst_1: sorted([i for i in lst_1 if i > 0]) + sorted([i for i in lst_1 if i < 0])
arranged_list = my_func(lst_1)
print(list(arranged_list))
