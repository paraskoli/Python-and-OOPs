# from posixpath import split
# import string


# this="    this is strip"
# print(this)
# print(this.strip()) #remove the space of this

def remove_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
this="  harry is a good boy"
n=remove_split(this,"harry")
print(n)
