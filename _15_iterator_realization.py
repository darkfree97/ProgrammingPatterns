# Шаблон проектування Iterator ( Ітератор )
"""
Інтерфейс який надає доступ до елементів об'єкту,
та можливість перебору цих елементів,
не розкриваючи їх внутрішню структуру об'єкту.
"""
from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def prev(self):
        pass

    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def is_begin(self) -> bool:
        pass

    @abstractmethod
    def is_end(self) -> bool:
        pass


class IteratorUser(metaclass=ABCMeta):
    @abstractmethod
    def get_iterator(self):
        pass


class AgreementIterator(Iterator):
    def __init__(self, arr: list):
        self.len = len(arr)
        self.index = 0
        self.array = arr

    def value(self):
        return self.array[self.index]

    def next(self):
        if not self.is_end():
            self.index += 1
            return self.array[self.index - 1]
        return self.array[self.index - 1]

    def prev(self):
        if not self.is_begin():
            self.index -= 1
            return self.array[self.index + 1]
        return self.array[self.index + 1]

    def begin(self):
        self.index = 0
        return self.value()

    def end(self):
        self.index = self.len - 1
        return self.value()

    def is_end(self) -> bool:
        return self.index == self.len

    def is_begin(self) -> bool:
        return self.index == -1


class AgreementsResultSet(IteratorUser):
    def __init__(self):
        self.arr = []
        self.arr.append("Угода - 1")
        self.arr.append("Угода - 2")
        self.arr.append("Угода - 3")
        self.arr.append("Угода - 4")

    def get_iterator(self):
        return AgreementIterator(self.arr)


if __name__ == '__main__':
    rs = AgreementsResultSet()
    _ = rs.get_iterator()
    print("Reverse")
    _.end()
    for i in range(_.len+1):
        print(_.prev())
    print("Normal")
    _.begin()
    for i in range(_.len+1):
        print(_.next())
