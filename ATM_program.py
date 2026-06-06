balance=15000
PIN1=5544
print("           -----WELCOME TO XYZ BANKING SYSTEM------")
print("""1-WITHDRAWAL
2-CHECK BALANCE
3-DEPOSIT
4-EXIT
""")
print("\n")

PIN=int(input("ENTER YOUR PIN:"))
if PIN1 == PIN :
            print("CORRECT PIN")
else :
            print("--WRONG PIN--")
            print("")
choice=int(input("ENTER THE CHOICE:"))
if choice==1:
    print("WITHDRAWAL")
    withdrawal=int(input("amount to be withrawal:"))
    
    if withdrawal > balance :
        print("balance run off")
    elif withdrawal < balance :
        balance-=withdrawal
        print("available balance:",balance)
    
elif choice==2:
    print("CHECK BALANCE")
    print("YOUR AVAILABLE BALANCE: ",balance)
elif choice==3:
    print("DEPOSIT")
    deposit=int(input("AMOUNT TO BE DEPOSIT:"))
    balance+=deposit
    print("AVAILABLE BALANCE:",balance)
elif choice==4:
    print("EXIT")
else :
   print("--**INVALID CHOICE**--")


