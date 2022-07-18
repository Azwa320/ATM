from cmath import pi


class Atm (object):
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def cashWithdrawl(self,amount):
        newAmount=50000-amount
        print("You have withdrawn amount"+str(amount)+"Your remaining balance is"+str(newAmount))
    def checkBalance(self):
        print("Your balance is 50000")
def main():
    cardnumber=input("insert your card number")  
    pinnumber=input("enter your pin number")  
    newUser=Atm(cardnumber,pinnumber)
    print("choose your activity")
    print("1.balance inquiry 2.withdrawal")
    activity=int(input("enter the activity number"))
    if activity==1:
        newUser.checkBalance()
    elif activity==2:
        amount=int(input("enter the amount"))  
        newUser.cashWithdrawl(amount)
    else:
        print("enter a valid number")  
if __name__=="__main__":
    main()           