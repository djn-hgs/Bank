import datetime
from dataclasses import dataclass, field
from hashlib import sha256


@dataclass
class Person:
    first_name: str
    last_name: str
    sex: str
    date_of_birth: datetime.date

    def __str__(self):
        return f'{self.last_name}, {self.first_name} ({self.date_of_birth})'



@dataclass
class BankAccount:
    account_number: int
    owners: [Person] = field(default_factory=list)
    balance: float = 0
    password_hash = ''

    def credit(self, amount: float):
        self.balance += amount

    def debit(self, amount: float):
        self.balance -= amount

    def set_password(self, pwd: str):
        self.password_hash = sha256(pwd.encode('utf-8')).hexdigest()

    def check_password(self, pwd: str):
        return sha256(pwd.encode('utf-8')).hexdigest() == self.password_hash

    def __str__(self):
        return str(self.account_number)


# TODO: Implement available fund checking

@dataclass
class Bank:
    accounts: ['BankAccount'] = field(default_factory=list)
    log: {datetime.datetime: str} = field(default_factory=dict)

    def log_event(self, message: str):
        now = datetime.datetime.now()
        self.log[now] = f'{now}: {message}'

    def credit_account(self, account: 'BankAccount', amount: float):
        account.credit(amount)
        self.log_event(f'Credited {amount} to account: {account}')

    def debit_account(self, account: 'BankAccount', amount: float):
        account.debit(amount)
        self.log_event(f'Debited {amount} from account: {account}')

    def transfer_money(self, from_account: BankAccount, to_account: BankAccount, amount: float):
        from_account.debit(amount)
        to_account.credit(amount)
        self.log_event(f'Transferred {amount} from account: {from_account} to account: {to_account}')

    def get_account(self, account_number: int):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

    def set_password(self, account: BankAccount, pwd: str):
        if account not in self.accounts:
            raise Exception('Unknown account')

        account.set_password(pwd)

    def authenticate(self, account: BankAccount, pwd: str):
        if account not in self.accounts:
            raise Exception('Unknown account')

        return account.check_password(pwd)

    def get_balance(self, account: BankAccount):
        if account not in self.accounts:
            raise Exception('Unknown account')

        return account.balance
