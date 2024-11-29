class Bankaccount:
    def __init__(self,account_no,name,account_type):
       self.account_no=account_no
       self.name=name
       self.account_type=account_type
       self.balance=0
       self.amount=0
    def deposit(self,amount):
       self.amount=amount
       self.balance+=amount
    def withdraw(self,amount):
       self.amount=amount
       if self.balance<self.amount :
          print("No sufficient balance to withdraw!!")
          return 0
       else:
         self.balance-=self.amount
         return 1
    def balanceDisplay(self):
      print(f"\nAvailable Balance: {self.balance}\n")


print("\n----Create account----")
acno=int(input("Enter the account number: "))
acname=input("Enter the owner name: ")
actype=input("Enter the account type(Savings/checking/current): ")

member=Bankaccount(acno,acname,actype)
while 1:
   choice=int(input("\nChoose a operation\n1.Deposit\n2.Withdraw\n3.Display Balance\n4.Exit\nChoice: "))
   if choice == 1:
       amount = int(input("\nEnter the amount to deposit:"))
       member.deposit(amount)
   elif choice == 2:
      amount = int(input("\nEnter the amount to withdraw:"))
      member.withdraw(amount)
   elif choice == 3:
      member.balanceDisplay()
   else:
      exit()

    
          
    
