import os

os.system("cls")

accounts = {}
balances = {}
next_account_number = 10000

def open_new_account():
    global next_account_number

    name = input("Enter the name of this account: ")
    phone_number = input("Enter your phone number: ")
    
    account_number = next_account_number
    next_account_number += 1
    
    accounts[account_number] = {'name': name, 'phone_number': phone_number}
    balances[account_number] = 0
    print(f"Account created successfully! Your account number is {account_number}")

def show_balance():
    owner_number = int(input("Enter your account number: "))
    owner_name = input("Enter your name: ")

    if owner_number in accounts and accounts[owner_number]['name'] == owner_name:
        print(f"Your balance is {balances[owner_number]:.2f}")
    else:
        print("Invalid account number or name")

def deposit():
    owner_number = int(input("Enter your account number: "))
    owner_name = input("Enter your name: ")

    if owner_number in accounts and accounts[owner_number]['name'] == owner_name:
        amount = int(input("Enter the amount you want to deposit: "))
        if 0 < amount < 1000000:
            balances[owner_number] += amount
            print(f"Amount deposited successfully! Your new balance is {balances[owner_number]:.2f}")
        else:
            print("Invalid amount, please enter a valid number")
    else:
        print("Invalid account number or name")

def withdraw():
        owner_number = int(input("Enter your account number: "))
        owner_name = input("Enter your name: ")

        if owner_number in accounts and accounts[owner_number]['name'] == owner_name:
            amount_to_withdraw = int(input("Enter the amount you want to withdraw: "))
            if amount_to_withdraw <= balances[owner_number]:
                balances[owner_number] -= amount_to_withdraw
                print(f"Amount withdrawer  successfully! Your new balance is {balances[owner_number]:.2f}")
            else:
                print("Invalid amount, please enter a valid number")
        else:
            print("Invalid account number or name")


def main():
    while True:
        print("Banking System Menu:")
        print("1. Open New Account")
        print("2. Show Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            open_new_account()
        elif choice == '2':
            show_balance()
        elif choice == '3':
            deposit()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()