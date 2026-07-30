# Leaky Bank Account

This repository contains a simple leaky-bucket style bank account example in Python.

Features
- Deterministic leak of balance over time (leak rate in currency units per second)
- Deposit and withdraw operations with basic validation
- Unit tests using pytest

Running tests

1. Install pytest if you don't have it:

   pip install pytest

2. Run tests from the repository root:

   pytest -q

Design notes
- The LeakyBankAccount accepts an optional time_provider callable (default: time.time)
  to make behavior deterministic in tests.

- The leak is applied lazily whenever balance is read or an operation occurs.
