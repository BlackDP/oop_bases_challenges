"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username):
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            print('Такого пользователя не существует.')
            
class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        self.usernames.clear()
        return self.usernames


if __name__ == '__main__':
    add_user1 = UserManager()
    add_user1.add_user('Nik')
    print(add_user1.get_users())
    
    add_user2 = AdminManager()
    add_user2.add_user('Sally')
    add_user2.add_user('Nik')
    print(add_user2.get_users())
    add_user2.ban_username('Niki')
    add_user2.ban_username('Nik')
    print(add_user2.get_users())
    
    add_user3 = SuperAdminManager()
    add_user3.add_user('Sally')
    add_user3.add_user('Nik')
    print(add_user3.get_users())
    add_user3.ban_username('Niki')
    add_user3.ban_username('Nik')
    print(add_user3.get_users())
    add_user3.ban_all_users()
    print(add_user3.usernames)