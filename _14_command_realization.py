# Шаблон проектування Команда ( Command )
import datetime
from abc import ABCMeta, abstractmethod


class ClientDataBase:
    def __init__(self):
        self.log = []
        self.users = set()

    def print_log(self):
        print("----------Log info-----------")
        if len(self.log) is 0:
            print("Log is empty")
        else:
            for query in self.log:
                print(query)
        print("-----------------------------")


class Command(metaclass=ABCMeta):
    @abstractmethod
    def do(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass


class CreateClient(Command):
    def __init__(self, surname: str, name: str, database: ClientDataBase):
        self.surname = surname
        self.name = name
        self.database = database
        self.executed_status = False
        self.execution_date = None

    def redo(self):
        if self.executed_status:
            self.undo()
            self.set_surname()
            self.set_name()
            self.do()
        else:
            print("Cannot do any change! Client was not added to database.")

    def undo(self):
        if self.executed_status:
            self.database.users.remove((self.surname, self.name))
            print(self.name + " " + self.surname + " was removed from database")
            self.executed_status = False
            self.database.log.remove(self)
        else:
            print("Cannot do any change! Client was not added to database.")

    def do(self):
        if self.executed_status is False:
            self.database.users.add((self.surname, self.name))
            print(self.name + " " + self.surname + " was added to database")
            self.executed_status = True
            self.database.log.append(self)
            self.execution_date = datetime.datetime.now()
        else:
            pass

    def set_name(self):
        temp = input("Input new name of client: ")
        if len(temp) is 0:
            print("Name not changed")
        else:
            self.name = temp

    def set_surname(self):
        temp = input("Input new surname of client: ")
        if len(temp) is 0:
            print("Surname not changed")
        else:
            self.surname = temp

    def __str__(self):
        return str(self.execution_date)+" "+self.surname+" "+self.name


if __name__ == '__main__':
    db = ClientDataBase()
    command = CreateClient("Lightman", "Cal", db)

    command.do()
    print(db.users)
    db.print_log()

    command.redo()
    print(db.users)
    db.print_log()

    command.undo()
    print(db.users)
    db.print_log()

