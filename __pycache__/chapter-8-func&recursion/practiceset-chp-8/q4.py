num=int(input("enter value of num:"))
def recur_sum(num):
    if num<=1:
        return num
    else:
        return num+recur_sum(num-1)
if num<0:
    print("enter a positive number")
else:
    print("the sum is",recur_sum(num))
    