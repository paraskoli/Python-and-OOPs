#Creating an empty set
# b=set()
# print(type(b))
 
# #adding value to the set
# b.add(4)
# b.add(5)
# print(b)


a={45,54,78,25}
# a.add([4,5,5]) #we can not add list to set
# print(type(a))
a.add(545)
print(a)
a.add((4,5,6)) 

#a.add({4:5}) #cannot add list or dictionary to sets

#length of set
print(len(a)) #print the length of a

#removal
a.remove(45) #remove 45 from set
#a.remove(15) #throws an error while trying to remove 15 (which is not present in set)
print(a)

print(a.pop()) #remove a element from begining 
print(a)
print(a.pop())
print(a)