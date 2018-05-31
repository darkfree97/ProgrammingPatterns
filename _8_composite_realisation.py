# Шаблон проектування Компонувальник ( Composite )
from abc import ABC, abstractmethod


def deep_of_tree(arg):
    if isinstance(arg, DepartmentManager):
        if arg.subordinates:
            return 1 + max([deep_of_tree(item) for item in arg.subordinates])
    return 1


class Agent(ABC):
    surname = None
    name = None

    def __init__(self, surname: str, name: str):
        self.surname = surname
        self.name = name

    @abstractmethod
    def level(self):
        pass

    @abstractmethod
    def to_serve(self):
        pass


class DepartmentManager(Agent):
    def __init__(self, *args):
        super().__init__(*args)
        self.subordinates = []

    def get_all_subordinates(self):
        return self.subordinates

    def add_subordinate(self, subordinate: Agent):
        if isinstance(subordinate, DepartmentManager):
            for item in subordinate.subordinates:
                self.add_subordinate(item)
        self.subordinates.append(subordinate)

    def to_serve(self):
        print("Клієнта обслуговував Менеджер відділу зі страхування")

    def __str__(self):
        s = ""
        for subordinate in self.subordinates:
            s += "\n\t"+str(subordinate)

        return self.name+" "+self.surname

    def level(self):
        return deep_of_tree(self)


class SubordinateAgent(Agent):
    def to_serve(self):
        print("Клієнта обслуговував Звичайний агент зі страхування")

    def __str__(self):
        return self.name+" "+self.surname

    def level(self):
        return 1


if __name__ == '__main__':
    a = SubordinateAgent("shdgs", "sdgagsjh")
    b = DepartmentManager("sjdjsha", "msdjahsjdh")
    c = DepartmentManager("adjashdajhsj","shdjhas")
    d = DepartmentManager("shjdash","zjshj")
    b.add_subordinate(a)
    c.add_subordinate(b)
    c.add_subordinate(d)

    print(d.level())
