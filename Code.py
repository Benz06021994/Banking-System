class Bank:
    # class features
    bankname = "HDFC Bank"
    branch = "Cusat,Ernakulam,India"
    ifsc = "9895172"

    # class attributes
    # constructor for creation of bank account
    def __init__(self, username, address, pan, aadhar, account_number, pin, confirm_pin):
        self.username = username
        self.address = address
        self.pan = pan
        self.aadhar = aadhar
        self.account_number = account_number
        self.pin = pin
        self.confirm_pin = confirm_pin
        self.balance = 0.0

    def is_valid_login(self, input_account_number, input_pin):  # function to check the credentials.
        return self.account_number == input_account_number and self.pin == input_pin

    def deposit(self, amount):  # function for deposit
        self.balance += amount
        print(f'{amount} deposited successfully. Your current balance is {self.balance}')

    def withdraw(self, amount):  # function for withdraw
        if amount <= self.balance:
            self.balance -= amount
            print(f'{amount} withdrawn successfully. Your current balance is {self.balance}')
        else:
            print("Insufficient balance")

    def check_balance(self):  # function for checking balance
        print(f'Your account balance is {self.balance}')

    def info(self):  # function for account info
        print(f'Name: ', self.username)
        print(f'Bank: ', self.bankname)
        print(f'Branch: ', self.branch)
        print(f'Account No: ', self.account_number)
        print(f'IFSC code: ', self.ifsc)
        print(f'Address: ', self.address)
        print(f'PAN No: ', self.pan)
        print(f'AADHAR No: ', self.aadhar)


def main(username=None, address=None, pan=None, account_number=None, pin=None, confirm_pin=None):
    print(f'Welcome to {Bank.bankname}, {Bank.branch}\nPlease create your account to move forward')

    username = input('Enter Your name: ')
    address = input("Enter your address: ")
    pan = input('Enter your PAN number: ')
    aadhar = input('Enter your AADHAR No: ')
    account_number = int(input('Enter Your account number: '))
    pin = int(input('Enter a pin number: '))
    confirm_pin = int(input('Re-Enter the pin to confirm: '))

    my_account = Bank(username, address, pan, aadhar, account_number, pin, confirm_pin)
    if pin == confirm_pin:
        print(f'Hello {username} congrats! your account created successfully\n'
              f'Please login using your account number and pin ')
        sec_main(my_account)
    else:
        print("The pin doesn't match. Please refresh this page again to restart the account creation process ")


def sec_main(my_account):
    account_number = int(input("Enter your account number: "))
    input_pin = int(input("Enter your PIN: "))

    if my_account.is_valid_login(account_number, input_pin):
        print("Login successful!")
        while True:
            print('\nPlease Select any option if you want to continue or to stop this service select 5:')
            print('1.Deposit\n2.Withdraw\n3.Check Balance\n4.Full info\n5.Stop this service')
            option = input('Option :  ')

            if option == '1':
                amount = float(input('Enter the amount to deposit:'))
                my_account.deposit(amount)

            elif option == '2':
                amount = float(input('Enter the amount to withdraw:'))
                my_account.withdraw(amount)

            elif option == '3':
                my_account.check_balance()

            elif option == '4':
                my_account.info()

            elif option == '5':
                print('Thanks for using HDFC Bank....')
                break

            else:
                print('Invalid Option Please select a valid option')

    else:
        print("Invalid account number or PIN. Please Try again")
        sec_main(my_account)


main()
