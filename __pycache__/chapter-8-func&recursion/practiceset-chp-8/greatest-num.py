def greatest(n1,n2,n3):
    if (n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3
m=greatest(56,89,29)
print("the value of a greatest number is",m)
        
    