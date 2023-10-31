from pytest import fixture
import main
import datetime


@fixture
def test_person():
    return main.Person(
        first_name='Bob',
        last_name='Smith',
        sex='M',
        date_of_birth=datetime.date(year=1970, month=1, day=1)
    )


@fixture
def test_account(test_person):
    return main.BankAccount(
        account_number=1234,
        owners=[test_person]
    )


@fixture
def another_account(test_person):
    return main.BankAccount(
        account_number=5678,
        owners=[test_person]
    )


@fixture
def bank(test_account, another_account):
    return main.Bank(
        accounts=[
            test_account,
            another_account
        ]
    )


def test_initial_balance(test_account):
    assert test_account.balance == 0


def test_credit(bank, test_account):
    bank.credit_account(test_account, 100)
    assert test_account.balance == 100


def test_debit(bank, test_account):
    bank.debit_account(test_account, 100)
    assert test_account.balance == -100


def test_transfer(bank, test_account, another_account):
    bank.transfer_money(
        test_account,
        another_account,
        100
    )
    assert test_account.balance == -100 and another_account.balance == 100


def test_password(bank, test_account):
    bank.set_password(test_account, 'password')
    assert bank.authenticate(test_account, 'password')
