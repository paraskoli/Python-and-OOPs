# def func(num,num2):
#     print(num,num2)
# func(4,5)

# def cube(x):
#     return x*x*x
# print(cube(5))

# def power(num, x):
#     result =1
#     for i in range(x):
#         result =result*num
#     return result
# print(power(5,3))

# print(power(x=4,num=5))


# def multi_add(*args):
#     result =0
#     for x in args:
#         result=result+x
#     return result

# print(multi_add(5,8,9,7))


# def vh(x,y):
#     if x<y:
#         print ("x is less than y")
#     elif x==y:
#         print("x is equal to y")
#     else:
#         print("x is greater than y")
# vh(50,50)

# def main():
#     x=5
#     while(x<10):
#         print("hello world")
#         x=x+1
# main()

# def main():
#     for x in range(5,10):
#         print("hello world")
# main()

# days=["mon","tue","wed","thu",'fri',"sat",'sun']
# for d in days:
#     print(d)

# def main():
#     for x in range(5,10):
#         print("hello world")
#         if x==8:
#             continue
# main()

# import math

# print("the square root of 16 is",math.sqrt(16))
# print("the cube of 9 is ",math.cube(9))




# palindrom Programm


# def is_palindrome(tester):
#     if tester ==tester[::-1]:
#         return True
#     return False

# run = True
# while(run):
#     tester = input("Enter strings to test for palindrome or 'exist':")
#     if tester=="exist":
#         run=False
#         break

#     tester=tester.lower()

#     newstr=""
#     for x in tester:
#         if x.isalnum():
#             newstr += x
#     print("palindrome test:",is_palindrome(newstr))


# thestr = "Ogres are often foolhardy oafs"
# newstr = ""
# for i, c in enumerate(thestr):
#     if c == "o":
#         continue
#     if i > 20:
#         break
#     newstr += c
# print(newstr)

# def main():
#     myfile=open("textfile.txt","a+")
#     for i in range (10):
#         myfile.write("this is a text\n")
#     myfile.close()


# import os
# from os import path
# import datetime
# from datetime import date,time,timedelta
# import time

# def main():
#     print(os.name)



# from datetime import date
# from datetime import time
# from datetime import datetime
# def main():
#     today=date.today()
#     print("today date is ",today)



import calendar

c=calendar.TextCalendar(calendar.MONDAY)
str =c .formatmonth(2022,9)
print(str) 

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)


