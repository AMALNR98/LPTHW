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
print("Is it less or equel?",5<= -2)
# Variables and Name
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
print("We need to put about ", average_passengers_per_car,"in each car")
# More Variables and Printing
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

print(w+e)
print("hi")
# More printing
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
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))# What Was That
tabby_cat = "\tI'm tabbed in."
persian_cat ="I'm split\non a line."
backlash_cat = "I'm \\ a\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()
print(f"So, you're {age} old,{height} tall and {weight} heavy.")
#Prompting pepole
age = input('How old are you?')
height = input("How tall are you")
weight = input("How much do you weight")

print(f"So, you're {age}old, {height} tall and {weight} heavy.")
# Parameters, Unpacking, Variables
from sys import argv
# read the WYSS section for how to run this
print(argv)
script, first, second, third = argv


print("The script is calld:", script)
print("Your first variable is :",first)
print("Your second variable is :",second)
print("Your third variable is:", third) 
 
#Prompting and Passing
from sys import argv

from click import prompt

script, user_name =argv
prompt ='>'
print(f"Hi{user_name}, I'm the {script}script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
# Readin file
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the file name again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-c (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truecating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for tree lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Im going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()


# More files
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copining from{from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is{len(indata)} bytes long")

print(f"Does the output file is{len(indata)}")
print("Ready, hit RETURN to continue. CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alwright, all done.")

out_file.close()
in_file.close()
