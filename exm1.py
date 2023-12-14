a=int(input("enter a number"))
if(a==0):
  print("wrong input")
elif(a<0):
 for j in range(a,0):
   if(a%j==0):
     print("factors of a given number:",j)
else:

   for i in range(1,a+1):
       if(a%i==0):    

          print("factors of a given number:",i)
    
