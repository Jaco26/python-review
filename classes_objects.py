lottery_player = {
  'name': 'Rolf',
  'numbers': (4,6,3,1),
}

class LotteryPlayer:
  def __init__(self, name = 'jacob'):
    self.name = name
    self.numbers = (4,6,3,1)

  def totals(self):
    return sum(self.numbers)


player = LotteryPlayer('Caroline')

class Student:
  def __init__(self, name, school): # pass the object 'self' as the first parameter
    self.name = name
    self.school = school
    self.marks = []

  def average(self):
    return sum(self.marks) / len(self.marks)

  
  def go_to_school(self): 
    print('I am going to {}'.format(self.school))

  @classmethod
  def what_i_am(cls): # pass the Class 'Student' as a parameter
    print('I am a {}'.format(cls))

  @staticmethod
  def say_something():
    print('I say stuff')



anna = Student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(77)

print(anna.average())
anna.go_to_school()
anna.what_i_am()

anna.say_something()