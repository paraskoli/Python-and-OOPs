words=["donkey","kaddu","sonu"]
with open('files.txt') as f:
    t=f.read()
for word in words:
    t=t.replace(word,"hello")
    with open("files.txt","w") as f:
        f.write(t)
 