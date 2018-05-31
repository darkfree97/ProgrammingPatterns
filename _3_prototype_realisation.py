# Шаблон проектування Прототип ( Prototype )
from abc import ABC, abstractmethod
from _1_factory_method_realization import HealthInsurance, PropertyInsurance
import copy


class InsurancePolicy(ABC):
    __insurance = None
    __client_name = None

    @abstractmethod
    def clone(self):
        pass

    def get_insurance(self):
        return str(self.__insurance)

    def get_client_name(self):
        return str(self.__client_name)

    def set_insurance(self, insurance):
        self.__insurance = insurance

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def __str__(self):
        return "Страхова угода:" \
               "\n\tВид страховки - "+self.get_insurance() + \
               "\n\tКлієнт        - "+self.get_client_name()


class HealthInsurancePolicy(InsurancePolicy):
    def __init__(self):
        self.set_insurance(HealthInsurance())
        self.set_client_name("Name of Client")

    def clone(self):
        return copy.copy(self)

    def clone(self, new_client_name):
        _copy = copy.copy(self)
        _copy.set_client_name(new_client_name)
        return _copy


if __name__ == '__main__':
    print("__________________")
    policy = HealthInsurancePolicy()
    c_policy = policy.clone("Yuri Gagarin")
    print(policy)
    print(c_policy)
    print("__________________")
    policy.set_insurance(PropertyInsurance())
    print(policy)
    print(c_policy)
