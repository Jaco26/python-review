# a decorator is a function that gets called before another function
import functools

def my_decorator(func):
  @functools.wraps(func)
  def function_that_runs_func():
    print('In the decorator!')
    func()
  return function_that_runs_func

@my_decorator
def my_decorated_func():
  print('I am the function!')

my_decorated_func()


## Decorators that take arguments
def decorator_with_args(number):
  def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func(*args, **kwargs):
      print('in the decorator')
      if number == 56:
        print('not runnning the function')
      else:
        func(*args, **kwargs)
      print('after the decorator')
    return function_that_runs_func
  return my_decorator


@decorator_with_args(54)
def my_func_too(x, y, name, hobby):
  print('Hello', x + y, hobby, name)


my_func_too(77, 33, hobby="Coding", name="Jacob")
