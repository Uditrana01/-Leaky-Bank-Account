import pytest
from leaky_bank_account import LeakyBankAccount

class FakeTime:
    def __init__(self, start: float = 0.0):
        self._t = start
    def now(self):
        return self._t
    def advance(self, seconds: float):
        self._t += seconds


def test_deposit_and_withdraw():
    t = FakeTime(100.0)
    acct = LeakyBankAccount(leak_rate=0.0, time_provider=t.now)
    acct.deposit(100)
    assert acct.balance == pytest.approx(100)
    ok = acct.withdraw(30)
    assert ok is True
    assert acct.balance == pytest.approx(70)


def test_overdraft_returns_false_and_does_not_change_balance():
    t = FakeTime(200.0)
    acct = LeakyBankAccount(leak_rate=0.0, time_provider=t.now)
    acct.deposit(50)
    ok = acct.withdraw(100)
    assert ok is False
    assert acct.balance == pytest.approx(50)


def test_leak_over_time():
    t = FakeTime(0.0)
    acct = LeakyBankAccount(leak_rate=1.0, time_provider=t.now)
    acct.deposit(10)
    assert acct.balance == pytest.approx(10)
    t.advance(3.0)
    assert acct.balance == pytest.approx(7.0)


def test_leak_never_negative():
    t = FakeTime(0.0)
    acct = LeakyBankAccount(leak_rate=5.0, time_provider=t.now)
    acct.deposit(8)
    t.advance(1.0)
    assert acct.balance == pytest.approx(3.0)
    t.advance(1.0)
    # after another second it should be 0, not negative
    assert acct.balance == pytest.approx(0.0)


def test_negative_deposit_raises():
    acct = LeakyBankAccount()
    with pytest.raises(ValueError):
        acct.deposit(-10)


def test_negative_withdraw_raises():
    acct = LeakyBankAccount()
    with pytest.raises(ValueError):
        acct.withdraw(-5)
