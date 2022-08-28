# n!=1*2*3*3*4*....n
"""n=int(input("enter the number"))
product=1
for i in range(n):
    product=product*(i+1)
print(product)"""

# def factorial(n):
#     product=1 
#     for i in range(n):
#         product=product*(i+1)
#     return product

def factorial1(n):
    if n==1 or n==0:
        return 1
    return n*factorial1(n-1)
f=factorial1(5)
print(f)

# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#     return n*factorial_recursive(n-1)
# f=factorial_iter(5)
# print(f)