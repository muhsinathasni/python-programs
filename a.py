list1=[]
count=0
n=int(input("enter a limit:"))
i=0
while i<n:
     i=i+1
     inp=input("enter a name:")
     list1.append(inp)
print("list is",list1)
for name in list1:
   if 'a' in name:
       count=count+name.count('a')
print("the total number of 'a' in the list is ",count)

