f=open('me.txt','r') #by default the mode is r
data=f.read() #read the first 5 character of the file
print(data)
f.close()