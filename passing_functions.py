def methodception(another):
  return another()

def add_two_numbers():
  return 35 + 77

# print(methodception(add_two_numbers))

## lambda: an anonymous one-line function
print(methodception(lambda: 35 + 37))

my_list = [13, 44, 66, 433]

# my_list.remove(13) # remove 13

print(list(filter(lambda x: x != 13, my_list))) # filter method must be wrapped in the list() method in order to have a list returned

(lambda x: x * 3)(5) # declare function with one parameter, call it with 5 as argument
# does same thing as 
def f(x):
  return x * 3
f(5)

def not_thirteen(x):
  return x != 13

print(list(filter(not_thirteen, my_list)))

## The filter method does the same thing as list comprehension