my_list = [0,1,2,3,4,5]
an_equal_list = [x for x in range(6)]

multiply_list = [x * 3 for x in range(6)]

print(an_equal_list)
print(multiply_list)

print(9 % 2)

print([n for n in range(20) if n % 2 == 0])

people_you_know = ['Rolf', ' John', 'anna', 'GREG']
normalized_people = [person.strip().lower() for person in people_you_know]

print(normalized_people)

def who_you_know():
  people = input('Say who you know but seperated by commas')
  people_list = [p.strip()[0].upper() + p.strip()[1:].lower() for p in people.split(',')]
  print(people_list)


who_you_know()