#create a mapping of state to abbrevation
states = {
    'origon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

#creat a basic set of states and some cities in them
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL': 'Jacksonville',
}

#add some more cities``
cities['NY']='New York'
cities['OR']='Portland'

#printnout some cities
print('_'*10)
print("NY State has: ",cities['NY'])
print("OR State has: ",cities['OR'])

#print some states
print('_'*10)
print("Michigen's abbrivation is:",states['Michigan'])
print("Florida's abbrivation is:",states['Florida'])

#do it by using the state then cities dict
print('_'*10)
print("Micigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

#print every states abbrivation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{states} is abbrivated {abbrev}")

#print every city in state
print('-'*10)
for abbrev, city in list(states.items()):
    print(f"{abbrev} has the {city}")

#now do both at the same time
print('_'*10)
for state,abbrev in list(states.items()):
    print(f"{state} is abbrivated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('_'*10)
#safety get a abbrivation by state thet might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#get a city with a default value
city =cities.get('TX','does Not Exist')
print(f"The city for the state 'TX is :{city}")