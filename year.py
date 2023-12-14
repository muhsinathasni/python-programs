start=2000
list1=[]
end=int(input("enter end year"))
while start<=end: 
   if (start%4==0 and (start%100!=0 or start%400==0)):
      list1.append(start)
   start+=1
print("list of leap year in the given range  is",list1)
