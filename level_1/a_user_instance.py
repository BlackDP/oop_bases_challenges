"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    user1 = User(
        name='Иван',
        username='testUser1',
        age=24,
        phone='+79119111111',
    )
    print(f'Информация о пользователе: Имя: {user1.name}, Юзернэйм: {user1.username}, Возраст: {user1.age}, Телефон: {user1.phone}')

