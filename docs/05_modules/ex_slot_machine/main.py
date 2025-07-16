'''
Slot machine
1. Spin Row
2. Display row
3. Get Payout
'''

import random

def spin_row():
    symbols = [ '🍒',' 🍉','🍋','🔔','⭐']

    results = [random.choice(symbols) for symbol in range(3)]

    return results

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 1
        elif row[0] == '🔔':
            return bet * 2
        elif row[0] == '⭐':
            return bet * 5
    return 0

def main():
    balance = 100

    print("--------------------------------")
    print("----- Welcome to Slot App ------")
    print("--- Symbols: 🍒 🍉 🍋 🔔 ⭐---")
    print("--------------------------------")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print('Invalid option. Please enter a number!')
            continue

        bet = int(bet)

        if bet > balance:
            print("--------------------------------")
            print('Insufficient funds!')
            print("--------------------------------")
            continue

        if bet <=0:
            print("--------------------------------------")
            print('Invalid amount! Must be greater than 0')
            print("--------------------------------------")
            continue

        balance -= bet

        spin_row()

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print(f"Sorry you lost this round!")
        balance += payout

        play_again = input("Do you want to spin again (Y/N?):").upper()

        if play_again != 'Y':
            break

    print('--------------------------------------')
    print(f'Game over! Your balance is ${balance}')
    print('Thank you for playing! Goodbye!')
    print('--------------------------------------')


if __name__ == '__main__':
    main()
