class Bank:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder 
        self.balance=balance 
    def deposit(self):
        amount=int(input('amount to deposit:'))
        self.balance+=amount 


    def withdraw(self):
        amount=int(input("amount to withdraw :"))
        self.balance-=amount


    def check_balance(self):
        return self.balance 
details=[Bank("shaik sihaam anjum",8000),
         Bank("vardhan",500)]
details[0].check_balance()

    
    


                      









    
  

   
    
       
    
    

        



