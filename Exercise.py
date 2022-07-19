#A good First Program
print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("Yay! Printing.")
print("i;s much rather you 'not'.")
print('I"said"do not touch this.')
print("hello")
#Numbers and Math
print("I will now count my chickens:")
print("hens",25+30/6)
print("Roosters",100-25*3%4)
print("Now I will count the eggs")
print(3+2+1-5+4%2-1/4+1)
print("Is it true that 3+2<5-7?")
print(3+2<5-7)
print("what is 3+2",3+2)
print("what is 5-7",5-7)
print("Oh, that's why it's false.")
print("How about some more")
print("Is it greater?", 5> -2)
print("Is it greater or equal?",5 >= -2)
print("Is it less or equel?",5<= -2)# Variables and Name
cars = 100
space_in_a_car =4.0
drivers = 30
passengers = 90
cars_not_driven = cars- drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven


print("There are", cars, "cars available.")
print("There are only",drivers, "drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have " ,passengers,"to carpool today.")
print("We need to put about ", average_passengers_per_car,"in each car")# More Variables and Printing
my_name = 'Amal N R'
my_age = 24 #satyayittum
my_height = 64 #inches
my_weight = 158 #lbs
my_eyes = 'black'
my_teeth ='white'
my_hair = 'black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy")
print("Actually thats not too heavy.")
print(f"He's got {my_eyes} and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} deepending on the coffee")

#this line is tricky, try to get it exatly right
total = my_age + my_height + my_weight
print(f" If I dd {my_age}, {my_height}, and {my_weight} I get {total}.")# Strings and Text
type_of_people = 19
x =f"There are {type_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Is't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)print("hi")# More printing
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("."*10)  #what'd that do? it will print '.' 10 times

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5+ end6 , end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)