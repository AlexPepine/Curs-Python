# Tema 1 Data Structures

# print the initial list
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

# sort from least to greatest
my_list.sort()
print(my_list)

# sort from greatest to least
my_list.sort(reverse= True)
print(my_list)

my_list_slice = my_list[::-1]
print(my_list_slice)
my_list_slice = my_list[::1]
print(my_list_slice)
#divizabile cu 3
my_list_slice = my_list[1::3]
print(my_list_slice)