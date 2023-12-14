b=[11,22,32,44,51,65,71,82,91,48,40,36]
print("list items=",b)
for ev in b: 
   if(ev%2==0):
     b.remove(ev)
print("list items after removing even items=",b)                                             
