def remove_even(x):
  for i in x[:]:
   if(i%2)==0:
     x.remove(i)
  return x
a=[12,34,76,16]
print(remove_even(a))
