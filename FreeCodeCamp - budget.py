class Category:
  def __init__(self,name):
    self.name=name
    self.ledger=[]
  def deposit(self,amount,description=""):
    if amount<0:
      raise ValueError("Attempt to deposit a nonpositive amount")
    self.ledger.append({"amount":amount,"description":description})
  def get_balance(self):
    balance=0
    for movement in self.ledger:
      balance+=movement["amount"]
    return balance
  def check_funds(self,amount):
    # you need a balance to check it...
    balance=self.get_balance()
    return amount<=balance
  def withdraw(self,amount,description="",warning=False):
    if amount<0:
      raise ValueError("Attempt to withdraw a nonpositive amount")
    ExecutableMovement=self.check_funds(amount)
    if ExecutableMovement:
      self.ledger.append({"amount":-amount,"description":description})
    else:
      # That's not requested, but I prefer to print a warning when a strange operation
      # is attempted. That ruins output appearance, so I left the user the ability
      # to turn it on
      if warning:
        print("Not enough money!")
    # at this point what was executable has been executed...
    return ExecutableMovement
  def transfer(self,amount,target):
    if amount<0:
      raise ValueError("Attempt to transfer a nonpositive amount")
    # Setup description
    des1="Transfer to "+target.name
    des2="Transfer from "+self.name
    # if there is money enough the movement is done
    WithDrawAttempt=self.withdraw(amount,des1)
    if WithDrawAttempt:
      target.deposit(amount,des2)
    return WithDrawAttempt
  def __str__(self):
    localname=self.name
    if len(localname)>30:
      localname=self.name[0:30]
    header=localname.center(30,"*")+"\n"
    footer="Total: "+str(self.get_balance())
    class_string=header
    for movement in self.ledger:
      linedes=movement["description"]
      if len(linedes)>23:
        linedes=linedes[0:23]
      linemoney=format(movement["amount"],"7.2f")
      class_string+=(linedes.ljust(23)+linemoney+"\n")
    class_string+=footer
    return class_string
  def total_withdrawals(self):
    # that's not requested but is useful to create the chart...
    tot_with=0
    for movement in self.ledger:
      if movement["amount"]<0:
        tot_with-=movement["amount"]
    return tot_with

def create_spend_chart(categories):
  Bins=[0]*len(categories)
  TotalWith=0
  MaxLenName=0
  for i in range(len(categories)):
    Bins[i]=categories[i].total_withdrawals()
    TotalWith+=Bins[i]
    if len(categories[i].name)>MaxLenName:
      MaxLenName=len(categories[i].name)
  for i in range(len(categories)):
    Bins[i]=int(10.0*Bins[i]/TotalWith)
    print(Bins[i])
  # We now have the height of the bins.
  # In order to print we will work first horizontally and ven vertically
  header="Percentage spent by category"
  col1="1           "+" "*MaxLenName
  col2="0987654321  "+" "*MaxLenName
  col3="00000000000 "+" "*MaxLenName
  col4="||||||||||| "+" "*MaxLenName
  interC="           -"+" "*MaxLenName
  # We are now ready to compose our horizontal chart 
  # the plan is to rotate it afterwards
  Chart=[col1,col2,col3,col4]
  for i in range(len(categories)):
    Chart.append(interC)
    col="o"*Bins[i]+"o"
    col=col.rjust(11)+"-"+categories[i].name.ljust(MaxLenName)
    Chart.append(col)
    Chart.append(interC)
  Chart.append(interC)
  # we have now composed our chart and we need to rotate it
  OutChart=header
  for i in range(len(Chart[1])): #in good faith, Chart is a rectangle...
    row=""
    for j in range(len(Chart)):
      row=row+Chart[j][i]
    OutChart+=("\n"+row)
  return OutChart
