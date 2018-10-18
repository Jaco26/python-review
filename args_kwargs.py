def my_method(arg1, arg2):
  return arg1 + arg2

my_method(4, 5)

def my_long_method(arg1, arg2, arg3, arg4, arg5):
  return arg1 + arg2 + arg3 + arg4 + arg5

def my_list_addition(list_arg):
  return sum(list_arg)

my_list_addition([1,3,5,6])


## *args 

def addition_simplified(*args): # *args arguments are put into a list
  return sum(args)

print(addition_simplified(3,5,6,3,2,22,3,4))


## **kwargs

def what_are_kwargs(*args, **kwargs): # **kwargs arguments are put into a dictionary. kwargs must be passed in after any other (positional args)
  print('args', args)
  print('kwargs', kwargs)

what_are_kwargs(23, 24, 'Hello', name="Jacob", location="Here")