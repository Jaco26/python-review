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