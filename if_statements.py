# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")

# if person in known_people:
#   print("You know {}!".format(person))
# else:
#   print('You do not know {}'.format(person))

## Exercise

def who_do_you_know():
  # ask the user for a list of people they know
  # split the string into a list 
  # return the list
  people = input('Who do you know?')
  return people.split(' ')

def ask_user(people_list):
  # ask the user for a name
  # see if the name is in the list of people they know
  # print out that they know the person
  name = input('Hey, give me a name. Any name.')
  if name in people_list:
    print('Hey neat! You know {}'.format(name))
  else:
    print('Oh, {} is\'t in the list'.format(name))
 


people = who_do_you_know()

ask_user(people)