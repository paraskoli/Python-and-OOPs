with open("log.txt") as f:
    t=f.read()
if "python" in t.lower() :
    print("yes python is present ")