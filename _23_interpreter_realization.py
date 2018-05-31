# Шаблон проектування Interpreter ( Інтерпретатор )
from abc import ABCMeta, abstractmethod
import re


class Clerk:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Controller(metaclass=ABCMeta):
    @abstractmethod
    def execute_command(self, *args):
        pass


class HumanSyntaxController(Controller):
    def __init__(self):
        self.clerks = [Clerk("Abraham Lincoln", "Health"), Clerk("Winston Cherchil", "Property")]
        self.clients = [Client("Abraham Lincoln", 67), Client("Winston Cherchil", 45)]

    def execute_command(self, *args):
        if isinstance(args[0], str):
            if re.search(r'(get|select|повернути|вибрати)', str(args[0]).lower()) is not None:
                if re.search(r'(list|список)', str(args[0]).lower()) is not None:
                    if re.search(r'(clients|клієнтів)', str(args[0]).lower()) is not None:
                        return self.clients
                    elif re.search(r'(clerks|клерків|agents|агентів)', str(args[0]).lower()) is not None:
                        return self.clerks
                else:
                    return "I can't return anything, check your sentences: " + args[0]
            else:
                return "Command is wrong"


if __name__ == '__main__':
    c = HumanSyntaxController()
    print(c.execute_command(input("Input your command: ")))
