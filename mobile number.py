'''
name:Nicole Nelson
a python program to code mobile number
'''
def valid_mobile_number():
    length=len(mobile1)
    if length==10 and mobile1[0] in "789":
        print("valid")
    else:
        print("invalid")
mobile1=input("enter the number:")
valid_mobile_number()