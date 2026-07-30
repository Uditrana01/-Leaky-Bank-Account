"""Leaky Bank Account implementation.

A simple leaky-bucket-style bank account where the balance decays over time
at a constant leak_rate (units: currency per second).

The account accepts a time_provider callable for deterministic testing.
"""
from typing import Callable, Optional
import time

class LeakyBankAccount:
    def __init__(self, leak_rate: float = 0.0, time_provider: Optional[Callable[[], float]] = None):
        """Create a LeakyBankAccount.

        leak_rate: amount leaked per second (>= 0)
        time_provider: function returning current time in seconds (defaults to time.time)
        """
        if leak_rate < 0:
            raise ValueError("leak_rate must be >= 0")
        self._leak_rate = float(leak_rate)
        self._time = time_provider or time.time
        self._balance = 0.0
        self._last_time = self._time()

    def _apply_leak(self) -> None:
        now = self._time()
        elapsed = now - self._last_time
        if elapsed <= 0:
            self._last_time = now
            return
        leaked = self._leak_rate * elapsed
        self._balance = max(0.0, self._balance - leaked)
        self._last_time = now

    @property
    def balance(self) -> float:
        self._apply_leak()
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("deposit amount must be >= 0")
        self._apply_leak()
        self._balance += float(amount)

    def withdraw(self, amount: float) -> bool:
        if amount < 0:
            raise ValueError("withdraw amount must be >= 0")
        self._apply_leak()
        if amount <= self._balance:
            self._balance -= float(amount)
            return True
        return False

    def set_leak_rate(self, leak_rate: float) -> None:
        if leak_rate < 0:
            raise ValueError("leak_rate must be >= 0")
        self._apply_leak()
        self._leak_rate = float(leak_rate)
