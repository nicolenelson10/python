'''
name=Nicole Nelson
python program
'''
list1=[]
list2=[]
list1_size=int(input("enter the size of list1"))
print("enter the elements of list1:")
for i in range(list1_size):
    list1.append(int(input()))
list2_size=int(input("enter the size of list2"))
print("enter the elements of list2:")
for i in range(list2_size):
    list2.append(int(input()))
print(list1,list2)
merged_list=list1+list2
print(merged_list)
even_list=[]
odd_list=[]
for i in merged_list:
    if i %2==0:
       even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
even_list.sort()
odd_list.sort()
print(even_list)
print(odd_list)
merged_list2=even_list+odd_list
print(merged_list2)




