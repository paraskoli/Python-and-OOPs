from dataclasses import replace


f=open("files.txt",'r') 
t=f.read()
t=t.replace("donkey","######")
f=open("files.txt","w")
f.write(t)
