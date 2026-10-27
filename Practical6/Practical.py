class BankAccount:
    def __init__(self, holder, account_number, opening_balance=0.0):
        if not holder.strip():
            raise ValueError("Account holder cannot be blank")
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.holder = holder
        self.account_number = account_number
        self._balance = float(opening_balance)
    def get_balance(self):
        return self._balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
    def __str__(self):
        return (f"BankAccount({self.holder}, "
                f"balance=■{self._balance:.2f})")
    def __repr__(self):
        return (f"BankAccount(holder={self.holder!r}, "
                f"account_number={self.account_number!r}, "
                f"opening_balance={self._balance!r})")
    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented 
        return self._balance + other._balance
    # Extension Task 1: Transfer money between accounts

    def transfer_to(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Target must be a BankAccount")
        if self is other_account:
            raise ValueError("Cannot transfer to the same account")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        other_account._balance += amount

 
    
    
# Return combined balance without modifying either account.
account1 = BankAccount("Asha", "BA101", 1500)
account2 = BankAccount("Kabir", "BA102", 500)
account1.deposit(250)
account2.withdraw(100)
print(account1) # readable display
print(repr(account1)) # developer-oriented representation
print(account2) 
print(repr(account2))
print(account1.get_balance()) # 1750.0
print(account1 + account2) # 2150


print("\nTask-1")
# Test the transfer of Extension Task-2
account1.transfer_to(account2, 200)

print("Asha's balance:", account1.get_balance())
print("Kabir's balance:", account2.get_balance()) 

# Extension Task 2: Read-only balance property

BankAccount.balance = property(BankAccount.get_balance)
print("\n Task-2")
# Test the property
print("Asha's balance:", account1.balance)

# Extension Task 3: Student class

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"roll_number={self.roll_number!r}, "
            f"marks={self.marks!r})"
        )


# Test the Student class
student1 = Student("Om", 42, 100)
print("\nTask-3")
print(student1)
print(repr(student1))