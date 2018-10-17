class Student:
  def __init__(self, name, school): # pass the object 'self' as the first parameter
    self.name = name
    self.school = school
    self.marks = []

  def average(self):
    return sum(self.marks) / len(self.marks)

  @classmethod
  def friend(cls, origin, friend_name, salary):
    friend = cls(friend_name, origin.school, salary)
    return friend


anna = Student('Anna', 'Oxford')

# jacob = anna.friend('Jacob')


class WorkingStudent(Student):
  def __init__(self, name, school, salary):
    super().__init__(name, school) # call the parent class's init method
    self.salary = salary


anna = WorkingStudent('Anna', 'Oxford', 20.00)

print(anna.salary)

jacob = WorkingStudent.friend(anna, 'Jacob', 17.50)

print(jacob.salary)