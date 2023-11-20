"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance
        
    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount

class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    bank_account = BankAccount(
        owner_full_name='Feel Parrot',
        balance=2000
    )
    print(f'Владелец счета: {bank_account.owner_full_name}, баланс:{bank_account.balance}')
    bank_account.increase_balance(1000)
    print(f'Поздравляем, счет пополнен, ваш баланс:{bank_account.balance}')
    bank_account.decrease_balance(1500)
    print(f'Расход со счета, ваш баланс:{bank_account.balance}')
    credit_account = CreditAccount(
        owner_full_name='Db. Swift',
        balance=5000
    )
    print(f'Владелец счета: {credit_account.owner_full_name}, баланс:{credit_account.balance}')
    credit_account.increase_balance(8000)
    print(f'Поздравляем, счет пополнен, ваш баланс:{credit_account.balance}')
    credit_account.decrease_balance(13000)
    print(f'Расход со счета, ваш баланс:{credit_account.balance}')
    check_credit = credit_account.is_eligible_for_credit()
    if check_credit:
        print('Вам доступно персональное предложение по кредитованию')
    else:
        print('Спасибо что обратились к нам, но к сожалению, клиент вы так себе...')