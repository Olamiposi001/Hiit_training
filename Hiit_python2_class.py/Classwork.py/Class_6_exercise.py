"""
Write a program that allows the user to perform basic banking options e.g:
select an option:
1 for balance
2 for recharge
3 for transfer

it asks the user to if they want to perform another transaction after completing one.
There should be a default balance at the start of the transaction that gets deducted as transaction is performed

"""

balance = 3000000

while True:
    print("Select an option")
    print("select 1 to check balance")
    print("Select 2 to recharge")
    print("select 3 to transfer")
    
    option = input("select an option: ")
    
    if option == "1":
        print(f"Your balance is ${balance}")
    elif option == "2":
        recharge_amt = int(input("Enter the amount you want to recharge: $"))
        balance = balance + recharge_amt
        print(f"Your new balance is ${balance}")
    elif option == "3":
        name = input("Enter the name of the recepient: ")
        acct_num = input("enter the recipeint account number: ")
        amt = int(input("Enter the amount: "))
        balance = balance - int(amt)
        print(f"Your new balance is ${balance}")
    elif option > "3" or option < "1":
        print("Enter a valid option")
    another_transaction = input("Do you want to perform another transaction? (Y/N): ")
    if another_transaction == "Y":
        continue
    if another_transaction == "N":
        break
    if another_transaction != "Y" and another_transaction != "N":
        print("Enter a valid option")
    
    # correction to the code above
    
    
    balance = 200000
    
    another_transaction = True
    
    while another_transaction:
        print("Welcome to py Banking.........")
        print("----------------")
        print("Select an option")
        print("select 1 to check balance")
        print("Select 2 to recharge")
        print("select 3 to transfer")
        
        op_code = input("select an option: ")
        if op_code == "1":
            print(f"Your balance is ${balance}")
        elif op_code == "2":
            phone_number = input("Enter the phone number you want to recharge: ")
            amount = int(input("Enter the amount you want to recharge: $"))
            balance = balance - amount
            print("Recharge sucessful")
             