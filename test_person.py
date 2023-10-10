from footballAPI.main import Person 

def test_person():
   person = Person("John", "Doe", 25)
   assert person.first_name == "John"
   assert person.last_name == "Doe"
   assert person.age == 25
   assert person.full_name() == "John Doe"
   assert person.introduce() == "Hello, my name is John Doe and I am 25 years old."
   assert person.birthday() == "Happy Birthday, John! You are now 26 years old."
   assert person.introduce() == "Hello, my name is John Doe and I am 26 years old."
   assert str(person) == "Person(John, Doe, 26)"
   assert repr(person) == "Person(John, Doe, 26)"