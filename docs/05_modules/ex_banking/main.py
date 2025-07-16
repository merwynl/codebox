'''
Banking app
1. Show balance
2. Deposit
3. Withdraw
'''

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to deposit: "))
    if amount < 0 :
        print("--------------------------------")
        print('Invalid amount!')
        print("--------------------------------")
        return 0
    else:
        print("---------------------------------")
        print(f"You have deposited ${amount:.2f}")
        print("---------------------------------")
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: "))
    if amount > balance:
        print("--------------------------------")
        print('Insufficient funds!')
        print("--------------------------------")
        return 0
    elif amount < 0:
        print("--------------------------------")
        print('Amount must be more than 0!')
        print("--------------------------------")
        return 0
    else:
        print("--------------------------------")
        print(f"You have withdrawn ${amount:.2f}")
        print("--------------------------------")
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("--------------------------------")
        print("-----Welcome to Banking App-----")
        print("--------------------------------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw()
        elif choice == "4":
            is_running = False
        else:
            print("--------------------------------")
            print('Invalid option selected!')
            print("--------------------------------")
    print("Goodbye!")

if __name__ == '__main__':
     main()