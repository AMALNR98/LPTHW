## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ##Dog has-a name
        self.name = name
    
## Cat is- a animal
class Cat(Animal):

    def __init__(self, name):
        ##cat has-a name
        self.name = name

## Person is-a object
class Person (object):

    def __init__(self, name):
        ##Person has-a name
        self.name = name
        
        ##Person has-a pet of some kid
        self.pet = name

## Person is-a Employee
class Employee(Person):

    def __init__(self, name, salary):
        ## 
        super(Employee, self).__init__(name)
        ##Employee has salary
        self.salary = salary

##fish is-a Object
class Fish(object):
    pass

##Salmon is-a fish
class Salmon(Fish):
    pass

##Halibut is-a fish
class Halibut(Fish):
    pass


# rover is-a Dog    
rover = Dog("Rover")

##satan is a cat
satan = Cat("Satan")

##Mary is-a Person
mary = Person("Mary")

##Mary has-a pet
mary.pet = satan

##frank is Employee
frank = Employee("Frank",120000)

##frank has-a pet
frank.pet = rover


flipper = Fish()


course = Salmon()


harry = Halibut()