'''
author name:Nicole Nelson
date:29-10-2024
'''
n=int(input("enter the no of rows:"))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=" ")
    print(" ")