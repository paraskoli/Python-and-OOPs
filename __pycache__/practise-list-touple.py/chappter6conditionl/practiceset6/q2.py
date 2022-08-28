s1=int(input("enter the marks of student 1\n:"))
s2=int(input("enter the marks of student 2\n:"))
s3=int(input("enter the marks of student 3\n:"))

if(s1<33 or s2<33 or s3<33):
    print("you are fail because you score less than 33 marks in one or more than one subject")
elif(s1+s2+s3)/3 <40:
    print("you are fail because total percentage is less than 40")
else:
    print("congratulation you are passed")
