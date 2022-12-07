def main():   
    import time
    print(" Hello! Welcome to ABC Bank--")
    print("please wait while your card is being read-----")
    time.sleep(2)
    print("Enter your details--")
    name=input("enter your name")
    pin = int(input("Enter your pin:"))
    balance= int(input("Total Balance in your Account:"))
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
        
    print('Please Press 1 For Your Balance\n')
    print('Please Press 2 To Make a Withdrawl\n')
    print('Please Press 3 To Deposit in\n')
    print('Please Press 4 To Return Card\n')
    option = int(input('What Would you like to choose?'))
    print("Please wait your request is being proceed---------")
    time.sleep(3)
    if option ==1:
        print("Your Balance is ",balance)
    restart= input("Would you like to go back?")
    if restart in('No','no','N','n'):
        print("Thank You")
    else:
        main()
        elif option ==2:
            withdrawl=int(input("enter amount needs to be withdrawl"))
            if withdrawl<balance:
                left_balance=balance-withdrawl
                print("Your balance now in account is:",left_balance)
            else:
                print("Invalid amount")
            restart= input("Would you like to go back?")
            if restart in('No','no','N','n'):
                print("Thank You")
            else:
                other()
        elif option==3:
            deposit=float(input("enter the amount you want to deposit"))
            balance=balance+deposit
            print("Total Amount in Your Account",balance)
            restart= input("Would you like to go back?")
            if restart in('No','no','N','n'):
                print("Thank you")
            else:
                other()
        elif option == 4:
            print('Please wait while your card is Returned...\n')
    
        if balance < 5000:
            print("Low Balance")
        else:
            print("Thank you for the visit")
            print("Have a good day---")
main()
