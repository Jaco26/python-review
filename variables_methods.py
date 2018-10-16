a = 5
b = 10
my_variable = 99

# pick single or double and stick to it
string_variable = "This is a variable"
single_quotes = 'A string can also be defined using single quotes'

print(single_quotes)

## 

def my_print_method(my_argument):
  print(my_argument)

my_print_method("If you don't pass anything in, you'll get a TypeError")

def my_multiply_method(num_1, num_2):
  return num_1 * num_2

result = my_multiply_method(4, 5)
my_print_method(result)