"""Exception handling: custom exceptions and try/except/finally."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""


class Account:
    def __init__(self, balance: float = 0.0) -> None:
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )
        self.balance -= amount


if __name__ == "__main__":
    account = Account(balance=100)
    try:
        account.withdraw(150)
    except InsufficientFundsError as e:
        print(f"Error: {e}")
    finally:
        print(f"Final balance: {account.balance}")
