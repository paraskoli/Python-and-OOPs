f=open("C:\\Users\\paras\\OneDrive\\Desktop\\python\\chapter-9\\chapter-9-practice-set\\poems.txt","r")
t=f.read()
if "twinkle" in t:    
    print("twinkle is present in t")
else:
    print("twinkle is not present in t")
f.close()