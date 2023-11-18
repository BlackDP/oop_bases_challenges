"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income
    
    def reduce_balance(self, income: float):
        self.balance -= income
        if self.balance < 0:
            raise ValueError('Баланс не может быть отрицательным')
        # try:
        #     self.balance -= income   
        #     if self.balance < 0:
        #         raise Exception('Баланс не может быть отрицательным')
        #     return self.balance
        # except Exception as e:
        #     return e


if __name__ == '__main__':
    client1 = BankAccount(
        owner_full_name='Иванов Иван Иванович',
        balance=1000.00
    )
    client1.reduce_balance(500)
    print(client1.balance)
    client1.reduce_balance(1500)
    print(client1.balance)
