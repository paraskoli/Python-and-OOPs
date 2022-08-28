first_name="paras"
last_name= "koli"
# print(type(name))
# print(first_name+last_name)
# concatenation of two string
c=first_name+last_name
print(c)
#slicing of string
a="Harry"
print(a[0:4])
print(a[4:5])

print(a[5:2])
slicing=a[1:5]
print(slicing)
print(a[0:])
print(a[:5])

#negative indices
print(a[-4:-1])#it is same as [1:4]
print(a[-5:-1])

#slicing with skip value
word="amazing"
print(word[1:6:2])

d="paraskoli" #with skip value 1
print(d[1:9:3])

print(d[0:9:2])

print(a[0::2])
