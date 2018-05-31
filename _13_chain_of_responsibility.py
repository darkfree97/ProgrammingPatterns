from abc import ABCMeta, abstractmethod


class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password


class ILogInSystem(metaclass=ABCMeta):
    @abstractmethod
    def add_login_function(self, func):
        pass

    @abstractmethod
    def log_in(self, user:User):
        pass

database = {}


def check_if_do_not_exist(user: User):
    global database
    print("Перевірка чи користувач не зареєстрований")
    for login in database:
        if login == user.login:
            print("Користувач зареєстрований")
            return False
    print("Користувач не зареєстрований")
    return True


def registration(user: User):
    print("Реєстрація нового користувача")
    database[user.login] = user.password
    print("Користувача з логіном "+user.login+" зареєстровано")
    return True


def authorization(user: User):
    print("Авторизація")
    if database[user.login] == user.password:
        print("Користувача з логіном " + user.login + " авторизовано")
        return True
    else:
        print("Користувача з логіном " + user.login + " не авторизовано")
        return False


class LogInSystem(ILogInSystem):
    func = []

    def __init__(self, f=False):
        if f:
            self.func.append(check_if_do_not_exist)
            self.func.append(registration)
            self.func.append(authorization)

    def log_in(self, user: User):
        flag = True
        for method in self.func:
            if flag:
                flag = method(user)
            else:
                flag = True

    def add_login_function(self, func):
        self.func.append(func)


if __name__ == '__main__':
    clerk = User("ali_baba", "password")
    login_system = LogInSystem(True)
    login_system.log_in(clerk)
    print("__________________________________")
    login_system.log_in(clerk)

