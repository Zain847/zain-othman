#السؤال الاةل
#A
L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]
L3 = dict(zip(L1, L2))
print(L3)
#B
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("enter the number: "))
print("the number is: {factorial(num)}")
#c
L = ['network', 'bio', 'programming', 'physics', 'music']

B_items = [item for item in L if item.startswith('B')]
print(B_items)
#d
keys = range(11)
values = [i+1 for i in keys]
d = dict(zip(keys, values))
print(d)
#ألسؤال الثاني
binary_number = input("enter binary number: ")

decimal_number = 0
for digit in binary_number:
    decimal_number = decimal_number * 2 + int(digit)
print("decimal number is:", decimal_number)
#السؤال الثالث
import json

with open('quiz_data.json', 'r') as file:
    quiz_data = json.load(file)

total_questions = len(quiz_data)
correct_answers = 0
user_name = input("enter your name: ")

for question, answer in quiz_data.items():
    user_response = input(f"{question} ")
    if user_response.lower() == answer.lower():
        correct_answers += 1

result = (correct_answers / total_questions) * 100
print(" {correct_answers} of {total_questions} ")
print("your result is: {result:.2f}%")
quiz_results = {user_name: result}
with open('quiz_results.json', 'a') as file:
    json.dump(quiz_results, file)
    file.write('\n')
#السؤال الرابع
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance:.2f}"
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return super().__str__() + f"\nInterest Rate: {self.interest_rate * 100:.2f}%"
bank_account = BankAccount("123456789", "John Doe")
bank_account.deposit(1000)
print(bank_account)
bank_account.withdraw(500)
print(bank_account)
savings_account = SavingsAccount("987654321", "Jane Smith", 1000, 0.05)
savings_account.apply_interest()
print(savings_account)