# Шаблон проектування Memento ( Зберігач )
"""
Шоблон проектування який організовує можливість 
збереження стану або станів об'єкта для їх 
можливого відновлення.
"""
from abc import ABCMeta, abstractmethod


class Memento(metaclass=ABCMeta):
    def __init__(self):
        self.state = None
        self.saved_state = list()

    @abstractmethod
    def set(self, state):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def save_state(self):
        pass

    @abstractmethod
    def rollback(self):
        pass


class Client(Memento):
    def __init__(self, name=None, police=None):
        super().__init__()
        self.name = name
        self.state = police
        self.police = self.state

    def rollback(self):
        self.state = self.saved_state.pop()
        print("State is restored")

    def get(self):
        return self.state

    def save_state(self):
        self.saved_state.append(self.state)
        print("State is saved")

    def set(self, state):
        self.state = state
        print("State is changed")

    def __str__(self):
        return "Client: "+self.name+" Insurance: "+self.state

    def try_new(self, police):
        self.save_state()
        self.state = police

    def get_police(self):
        return self.get()


if __name__ == '__main__':
    client = Client(police="Страхування життя", name="Willy Wonka")
    print(client)
    print("---------------------------------------------------")
    client.try_new("Страхування власності")
    print(client)
    print("---------------------------------------------------")
    client.rollback()
    print(client)





