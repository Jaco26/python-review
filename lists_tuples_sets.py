# grade_one = 77
# grade_two = 88
# grade_and_so_on = 90

# # caluclate the average grade
# print((grade_one + grade_two + grade_and_so_on) / 3)

# # realistic way with a list
# grades = [77, 88, 90, 98, 87]

# print(len(grades))

# print(sum(grades) / len(grades))

# ## 

# # Tuple: just like a list EXCEPT IMMUTABLE!!!
# #   cannot increase the size of the tuple
# grades_tuple = ( 77, 88, 90, 98, 87 ) # print order is guaranteed

# ## 

# # Set: a collection of unique and unordered values
# grades_set = { 77, 88, 90, 98, 87 } # print order is NOT guaranteed

# print(grades_tuple)
# print(grades_set)


# ##

# # Helpful methods

# grades_list = [77, 88, 90, 98, 87]
# grades_tuple = ( 77, 88, 90, 98, 87 )
# grades_set = { 77, 88, 90, 98, 87 } 

# grades_list.append(67) # add 67 to end of list

# grades_tuple = grades_tuple + (100,) # create a new tuple with the value of the original plus another one with one element

# grades_list[0] = 60 # we can mutate lists by accessing an element by its index and reassign the value of that element
# print(grades_list[0])

# grades_tuple[0]  # we can NOT mutate tuples
# print(grades_tuple[0])

# # print(grades_set[0]) # we cannot access Set elements with an index because sets are unordered 
# grades_set.add(60) # we can still add values to a Set 



## Set operations
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11} 

# Are some elements in one Set present in another?
print(your_lottery_numbers.intersection(winning_numbers))

# Merge Sets
print(your_lottery_numbers.union(winning_numbers))

# The values in your_lottery_numbers that are NOT present in winning_numbers
print(your_lottery_numbers.difference(winning_numbers)) 