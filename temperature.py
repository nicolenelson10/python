'''
author name:Nicole Nelson
date:22-10-2024
'''
temp=int(input("enter the temperature:"))
t=input("is this in (C)elsius or (F)ahrenheit?")
if t=='C':
    f=( 9/5 * temp)+32
    print(temp,"is",f,"fahreinheit")
else:
    C=5/9 * (temp-32)
    print(temp,"is",C,"celcius")


