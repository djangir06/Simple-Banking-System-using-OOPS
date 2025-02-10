class bank:
    
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
    
   #Adding amount

    def deposit(self,depo_amt):

        self.amount += depo_amt 
        print(f"\nRs {depo_amt} is sucessfully added.")
        print(f"Now Current Balance: {self.amount}")
   
    #Withdraw

    def widrawal(self,widrawaal):

        if(self.amount > widrawaal):
        
            print("\nSucessfully done!!")
            print(f"Current Balance: {self.amount - widrawaal}")

        else:

            print("Unsufficient Balance!")

#User name

name = input("\nEnter your name: ")

x = bank(name,500)

print(f"\nHiii!! {name}")
print("Current Balance: 500")

#Random assignment for while loop

user_input = "carzy"

while user_input not in ["deposit", "withdraw"]:

    user_input = input("\nWhat you want to do? deposit or withdraw?: ")
    
    if user_input == "deposit":
       
        amount = int(input("\nEnter the amount you want to add: "))
        x.deposit(amount)
    
    elif user_input == "withdraw":
        
        w_amount = int(input("\nenter the widraw amount: "))
        x.widrawal(w_amount)

    else:

        print("Write withdraw or deposit")


print("\nThanks for visiting us!!")

