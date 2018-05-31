# Фабричний метод (Factory Method)
from abc import ABC, abstractmethod


class Insurance(ABC):
    @abstractmethod
    def __str__(self):
        pass


class HealthInsurance(Insurance):
    def __str__(self):
        return "Страхування життя"


class PropertyInsurance(Insurance):
    def __str__(self):
        return "Страхування власності"


class InsuranceCompany(ABC):
    @abstractmethod
    def __init__(self, insurance: Insurance):
        self.insurance = insurance

    @abstractmethod
    def __str__(self):
        pass

    def get_insurance(self):
        return self.insurance


class InsuranceCompanyA(InsuranceCompany):
    def __init__(self):
        super().__init__(HealthInsurance())

    def __str__(self):
        return "Медична страхова компанія"


class InsuranceCompanyB(InsuranceCompany):
    def __init__(self):
        super().__init__(PropertyInsurance())

    def __str__(self):
        return "Майнова страхова компанія"


if __name__ == '__main__':
    a = InsuranceCompanyA()
    print(a.get_insurance())
    b = InsuranceCompanyB()
    print(b.get_insurance())
