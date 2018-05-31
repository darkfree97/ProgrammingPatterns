# Шаблон проектування Декоратор ( Decorator )
from abc import ABCMeta, abstractmethod


class Document:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show_info(self):
        pass


class InsurancePolicy(Document):
    def __init__(self, name_of_insurance):
        self.__name_of_insurance = name_of_insurance

    def show_info(self):
        print(self.__name_of_insurance, end="")


class Agreement(Document):
    def __init__(self, policy: InsurancePolicy = None, client=None):
        self.__policy = policy
        self.__client = client

    def set_client(self, client=None):
        self.__client = client

    def show_info(self):
        print("Insurance:", end="\n\t")
        self.__policy.show_info()
        print("\nFor client: \n\t"+str(self.__client))


if __name__ == '__main__':
    agreement = Agreement(InsurancePolicy("Health insurance"), "Satoshi Nakamoto")
    agreement.show_info()












