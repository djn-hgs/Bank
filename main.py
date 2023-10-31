import datetime
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    sex: str
    date_of_birth: datetime.date


@dataclass
class BankAccount:
    account_number: int
    owners: [Person]
    balance: float


@dataclass
class Bank:
    accounts: [BankAccount]
    log: {datetime.datetime: str}




