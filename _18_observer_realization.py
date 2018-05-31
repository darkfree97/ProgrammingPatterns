# Шаблон проуктування Observer ( Спостерігач, Передплатник )
"""
Поведінковий шаблон проектування що забезпечує механізм,
який дозволяє об'єкту отримувати сповіщення від інших об'єктів.
Визначає залежність один до багатьх.
"""
from abc import ABCMeta, abstractmethod


# Той хто спостерігає
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def notify_message(self, data):
        pass

    @abstractmethod
    def delete_first_message(self):
        pass


# Той за ким спостерігають
class Observable(metaclass=ABCMeta):
    def __init__(self, observers=list()):
        self.observers = observers

    def register(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.notify_message(message)


class SpecialProposition(Observable):
    def __init__(self, observers=list()):
        super().__init__(observers)
        self.message = None

    def remove_oldest(self):
        for observer in self.observers:
            observer.delete_first_message()


class Client(Observer):
    def __init__(self, username):
        self.username = username
        self.messages = list()

    def __str__(self):
        return self.username

    def delete_first_message(self):
        try:
            self.messages = self.messages[1:]
        except IndexError:
            print("Yeah")

    def notify_message(self, data):
        self.messages.append(data)


def check(_server: Observable):
    for client in _server.observers:
        print(client)
        print("Messages:")
        for message in client.messages:
            print("#"+str(message))
        print("-----------------")

if __name__ == '__main__':
    client1 = Client("user1")
    client2 = Client("user2")
    client3 = Client("user3")
    server = SpecialProposition([client1, client2, client3])
    server.notify_observers("Holla Mundo")
    check(server)
    print("_________________________________________")
    server.notify_observers("Hello World")
    check(server)
    print("_________________________________________")
    server.remove_oldest()
    check(server)
    print("_________________________________________")






