"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
    
    def should_be_banned(self):
        if self.surname in SURNAMES_TO_BAN:
            return f'Пользователь забанен'
            # print('Пользователь забанен')
        return f'Все в порядке'
        
if __name__ == '__main__':
    user1 = User(
        name='Mike',
        surname='Wilhelm',
        age=35
    )
    check_user = user1.should_be_banned()
    print(check_user)
