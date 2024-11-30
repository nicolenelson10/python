'''
name:Nicole Nelson
program to accepts the lengths of three sides of a triangle as inputs
'''
def right_angle_triangle():

 empty_list=[]
 empty_list.append(side1)
 empty_list.append(side2)
 empty_list.append(side3)
 empty_list.sort()
 if empty_list[2]**2==empty_list[0]**2+empty_list[1]**2:
    print("the given sides are a part of the right angle triangle")
 else:
    print("the given sides are not a part of  the right angle triangle")

side1=int(input("enter the length of 1st side:"))
side2=int(input("enter the length of 2nd side: "))
side3=int(input("enter the length of 3rd side:"))
right_angle_triangle()