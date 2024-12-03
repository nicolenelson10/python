'''
name:Nicole Nelson
a python program to add 2 numbers
'''
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
print(add_numbers(4,5))