from account import Account


def main():
    account_1 = Account.get()
    account_1.deposit()
    print(account_1.balance)
    account_1.withdraw()
    print(account_1.balance)
    print()
    print(account_1)


if __name__ == "__main__":
    main()