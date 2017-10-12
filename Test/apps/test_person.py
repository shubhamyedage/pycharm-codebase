from apps.person_model import PersonModel


person = PersonModel('Shubham')


print(person.get_name())

person.name = 'Synerzip'
print(person.name)
