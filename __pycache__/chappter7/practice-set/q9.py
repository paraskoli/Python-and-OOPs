n=int(input("enter the number :"))
for i in range(n):
    for j in range(n):
      if (i==j==n-2):
         print('   ',end="")
      else:
          print('*  ',end="")
    print('\n')
