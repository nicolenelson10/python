'''
name:Nicole Nelson
a python program to find factorial
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
