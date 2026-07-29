import pytest
from bank_account import BankAccount


def test_deposit():
    account = BankAccount("Tejveer", 100)
    account.deposit(50)
    assert account.getBalance() == 150


def test_overdraw():
    account = BankAccount("Tejveer", 100)

    with pytest.raises(ValueError):
        account.withdraw(150)


def test_negative_withdrawal():
    account = BankAccount("Tejveer", 100)

    with pytest.raises(ValueError):
        account.withdraw(-50)