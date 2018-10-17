my_string = "hello" # iterable

# for loops can iterate over iterables
for character in my_string: # iterables are string, lists, sets, tuples and more
  print(character)


my_list = [1, 3, 5, 7, 9]

for number in my_list:
  print(number ** 2)


user_wants_number = True

while user_wants_number:
  print(10)
  answer = input('Do you want to see the number again? (y/n)')
  if answer != 'y':
    user_wants_number = False
 


