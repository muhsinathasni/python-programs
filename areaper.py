class Rectangle:
    def __init__ (self):
             self.l=float(input("enter length:"))
             self.b=float(input("enter breadth:"))
    def area(self):
             self.ar=self.l * self.b
             print("area=",self.ar)
    def perim(self):
        self.per=2*(self.l+self.b)
        print("perimter=",self.per)
print("rectangle1:")
r1=Rectangle();
r1.area()
r1.perim()
print("rectangle2:")
r2=Rectangle();
r2.area()
r2.perim()
if(r1.ar>r2.ar):
   print("rectangle 1 has greater area")
elif(r1.ar==r2.ar):
   print("rectangle have equal area")
else:
   print("rectangle2 has greter area")
