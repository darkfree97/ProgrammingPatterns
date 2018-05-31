# Шаблон проектування Visitor ( Відвідувач )
from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, visitor_user):
        pass


class VisitorUser:
    def accept(self, visitor: Visitor):
        visitor.visit(self)


class Clerk(VisitorUser):
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


class Client(VisitorUser):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PeopleParser(Visitor):
    def __init__(self):
        self.clerk_file = open("files/visitor_clerk.txt", "a")
        self.client_file = open("files/visitor_client.txt", "a")

    def __del__(self):
        self.clerk_file.close()
        self.client_file.close()

    def visit(self, visitor_user):
        if isinstance(visitor_user, Clerk):
            self.clerk_file.write("Clerk: {0} | Profession: {1}\n".format(visitor_user.name, visitor_user.profession))
        elif isinstance(visitor_user, Client):
            self.client_file.write("Client: {0} | Age: {1}\n".format(visitor_user.name, visitor_user.age))


if __name__ == '__main__':
    heap = Client("Mahmud", 40), Clerk("John", "Insurance agent")
    file_parser = PeopleParser()
    for man in heap:
        man.accept(file_parser)

