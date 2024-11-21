# Python Banking Program
# show balance, deposit, withdraw

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit():
    print("_-_-_-_-_-_-_-_-_")
    amount = float(input("Enter a amount to be deposited: "))
    print("_-_-_-_-_-_-_-_-_")
    if amount < 0:
        print("_-_-_-_-_-_-_-_-_")
        print("That's not a Valid amount")
        print("_-_-_-_-_-_-_-_-_")
        return 0
    else:
        return amount


def withdraw(balance):
    print("_-_-_-_-_-_-_-_-_")
    amount = float(input("Enter amount to be withdrawn: "))
    print("_-_-_-_-_-_-_-_-_")

    if amount > balance:
        print("_-_-_-_-_-_-_-_-_")
        print("Insufficient funds")
        print("_-_-_-_-_-_-_-_-_")
        return 0
    elif amount < 0:
        print("_-_-_-_-_-_-_-_-_")
        print("Amount must be greater than 0")
        print("_-_-_-_-_-_-_-_-_")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("_-_-_-_-_-_-_-_-_")
        print("Banking Program")
        print("_-_-_-_-_-_-_-_-_-_-_")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("_-_-_-_-_-_-_-_-_-_")
            print("That is not a valid choice")
            print("_-_-_-_-_-_-_-_-_-_-")
    print("_-_-_-_-_-_-_-_-_")
    print("Minnatwar!")
    print("_-_-_-_-_-_-_-_-_")
if __name__ == '__main__':
    main()
