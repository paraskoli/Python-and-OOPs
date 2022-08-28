from turtle import update


myDict={
    "Fast":"In a quick manner",
    "Paras":"A Coder",
    "Marks":[1,2,4,5],
     "anotherdict":{'harry':'player'},
     1:2
}
# print(list(myDict.keys())) #print the key of a dictionary
# print(myDict['Fast'])
# print(myDict["Marks"])
# print(myDict["Paras"])
# print(myDict["anotherdict"])
# print(list(myDict.values())) #print the values of a dictionary

# print(myDict.items()) #prints all the keys and the values of contents

#update a dictionary
print(myDict)
updateDict={
    "Paras":"koli",
    "mayank":"koli",
    "naresh":"kumar",
    "sonu":"kabir",
    "chaubay":"shubham"
}
myDict.update(updateDict) #update a dictionary by adding key value pairs in update dictionary
print(myDict)

print(myDict.get("sonu"))# print value associated with key sonu 
print(myDict["sonu"]) #  print value associated with key sonu 

# the difrence between .get and [] syntax in dictinaryprint
print(myDict.get("harry")) #return none as harry is not present in a dictionary
print(myDict["harry"]) #throws an error   