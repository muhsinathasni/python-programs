class Account:
  def __init__ (self,acc,name,type):
       self.balance=0
       self.acc=acc
       self.name=name
       if(type==1):
          self.type="current"
       else:
                self.type="savings"
  def deposit(self):
          amount=float(input("enter amount to be deposited:"))
          self.balance+=amount
  def withdraw(self):
           amount=float(input("enter amount to be withdrawn:"))
           if(self.balance<amount):
                print("insufficient balance")
           else:
                self.balance-+amount

  def display(self):
               print("name:",self.name,"\t\t account no:",self.acc,"\t \t balance:",self.balance,"\t\t acc:",self.type)
               acc=input("enter account number")
               name=input("enter name")
               type=input("choose account type:\n1.current \n2.savings")
               obj=Account(acc,name,type)
               while True:
                     obj.display()
                     ch=int(input("\n deposit 2.withdraw \n3.exit"))
                     if(ch==1):
                          obj.deposit()
                     elif(ch==2):
                           obj.withdraw()   

                     elif(ch==3):
                              break
                     else:
                            print("invalid entry") 
