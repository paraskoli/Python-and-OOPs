mydict={
    "khana":"food",
    "pankha":"fan",
    "vastu":"items"
}
print("options are",mydict.keys())
a=input("enter the hindi word\n")
#the below line thrwos an error if the key is not present in the dictionary
print("the meaning of your hindi word is",mydict.get(a))