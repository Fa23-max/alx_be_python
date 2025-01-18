class BankAccount:
  def _init_(self,account_balance = 0):
    self.account_balance = account_balance
    
  def deposit(self,amount):
    self.account_balance += amount

  def withdraw(self,amount):
    if amount > self.account_balance:
      return False
    else :
      self.account_balance -= amount
      return True
    
  def display_balance(self):
    print(f"Current Balance: ${self.account_balance}")