class Student:
  def __init__(self, name, school): # pass the object 'self' as the first parameter
    self.name = name
    self.school = school
    self.marks = []

  def average(self):
    return sum(self.marks) / len(self.marks)

  @classmethod
  def friend(cls, origin, friend_name, **args):
    friend = cls(friend_name, origin.school, *args)
    return friend


anna = Student('Anna', 'Oxford')

# jacob = anna.friend('Jacob')


class WorkingStudent(Student):
  def __init__(self, name, school, salary, job_title):
    super().__init__(name, school) # call the parent class's init method
    self.salary = salary
    self.job_title = job_title


anna = WorkingStudent('Anna', 'Oxford', 20.00, 'Software Person')

print(anna.salary)

jacob = WorkingStudent.friend(anna, 'Jacob', salary=17.50, job_title='Software Person')

print(jacob.salary)