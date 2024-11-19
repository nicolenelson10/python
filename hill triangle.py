'''
author name:Nicole Nelson
date:29-10-2024
'''
n=int(input("enter the  number of rows:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")

    for k in range(1,2*i):
        print("*",end=" ")
    print()