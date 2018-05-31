# Шаблон проектування Легковаговик ( Flyweight )
from _8_composite_realisation import *
from random import randrange


class Insurance:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)

    def __str__(self):
        return self.name


class Agreement:
    def __init__(self, insurance: Insurance, client, clerk_id):
        self.insurance = insurance
        self.client = client
        self.clerk_id = clerk_id

    def show_info(self, clerk):
        print("Страховка: ", str(self.insurance))
        print("Клієнт: ", str(self.client))
        print("Клерк: ", str(clerk))
        print("Вартість: ", self.insurance.price+(100*clerk.level()))


class Controller:
    def __init__(self):
        self.clerks = [DepartmentManager("Гудіні", "Гаррі")]
        self.clerks[0].add_subordinate(SubordinateAgent("Some", "Man"))
        self.agreements = [Agreement(Insurance("Страхування будинку", "3000"), "Законослухняний громадянин"
                                     , randrange(len(self.clerks)))]

    def print_agreements(self):
        print("++++++++++++++++++++++++++++++++")
        for agreement in self.agreements:
            agreement.show_info(self.clerks[agreement.clerk_id])

    def getattr(self, index, item):
        if index in range(len(self.agreements)):
            if item == "name":
                return self.agreements[index].insurance.name
            elif item == "client":
                return self.agreements[index].client
            elif item == "price":
                return self.agreements[index].insurance.price
            elif item == "clerk":
                return self.clerks[self.agreements[index].clerk_id]


if __name__ == '__main__':
    c = Controller()
    c.print_agreements()
    print(c.getattr(0, "clerk"))

    a = [1, 2, 3]
    b = a
    b[2] = 4
    print(a)





