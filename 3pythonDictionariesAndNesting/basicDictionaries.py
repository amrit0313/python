#1.dictionary creation

myDictionary = {
    "Bug":"error in a program",
    "Glance":"A slight view",
    "Next":"something after the present one",
    "First":"to come before everybody",
    123:"a random number"
}

#now to access a certain item in dictionary
myDictionary[123] #this would display a random number
myDictionary["Bug"]#this would display error in a program 

#now to add items to dictionary
myDictionary["Amrit"] = "this means elixir, a immortal drink"
# print(myDictionary) #all dictionary would be printed, including amrit

#we can also edit dictionary with this idea
myDictionary["Bug"] = "this refers to any program occurred in programming" #the value of bug will be this from now

#to start dictionary with empty dictionary
# myDictionary = {}   , this is commented coz this would wipe out all items in dictionary, so we can also wipe out items


#loop through dictionary

for key in myDictionary: #we know key isnt necessary here to write, but that would result in key in dictionary
    print(key)  #this would print keys
    print(myDictionary[key])  # this would print keys