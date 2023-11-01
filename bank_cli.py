import datetime
import bank

test_person = bank.Person(
    last_name='Noyce',
    first_name='Daryl',
    sex='M',
    date_of_birth=datetime.date(year=1975, month=10, day=28)
)

test_account = bank.BankAccount(1234, [test_person])
test_account.set_password('password')

another_account = bank.BankAccount(5678, [test_person])
another_account.set_password('qwerty')

test_bank = bank.Bank(accounts=[test_account, another_account])


selected_account: bank.BankAccount | None = None

while True:
    if selected_account:
        # Show actions for a selected account

        print(f'Selected account is {selected_account} with balance {selected_account.balance}')

        print(
            'Actions are:'
            '1: Credit money'
            '2: Debit money'
            '3: Balance enquiry'
            '4: Set password'
        )

        action = input('Action:')
        pwd = input('Password:')

        authenticated = test_bank.authenticate(test_account, pwd)

        if authenticated:
            if action == '1':
                amount = float(input('How much?'))
                test_bank.credit_account(selected_account, amount)
            elif action == '2':
                amount = float(input('How much?'))
                test_bank.debit_account(selected_account, amount)
            elif action == '3':
                balance = test_bank.get_balance(selected_account)
                print(f'Balance is {balance}')
            elif action == '4':
                new_pwd = input('New password:')
                test_bank.set_password(selected_account, new_pwd)
        else:
            print('Incorrect password. Try again.')
    else:
        # Actions if an account is not yet selected

        print(
            'Actions are:'
            '1: Select an account to interact with'
            '2: Create an account'
            '3: Delete an account'
        )

        action = input('Action:')
        if action == '1':
            account_number = int(input('Account number'))
            pwd = input('Password:')
            account = test_bank.get_account(account_number)

            if account:
                authenticated = test_bank.authenticate(account, pwd)
                if authenticated:
                    print('Authenticated')
                    selected_account = account
                else:
                    print('Authentication failure')
                    selected_account = None

            else:
                selected_account = None
                print('Not found. Try again')

        elif action == '2':
            ...
        elif action == '3':
            ...
