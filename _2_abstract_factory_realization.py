# Абстрактна фабрика ( Abstract Factory )
from abc import ABC, abstractmethod


class MainInsurance(ABC):
    @abstractmethod
    def __str__(self):
        pass


class HealthInsurance(MainInsurance):
    def __str__(self):
        return "Страхування життя"


class CarInsurance(MainInsurance):
    def __str__(self):
        return "Страхування автомобіля"


class AdditionalInsurance(ABC):
    @abstractmethod
    def __str__(self):
        pass


class PetsInsurance(AdditionalInsurance):
    def __str__(self):
        return "Страхування життя домашнього улюбленця"


class BikeInsurance(AdditionalInsurance):
    def __str__(self):
        return "Страхування мотоцикла"


class InsurancePackageFactory(ABC):
    @abstractmethod
    def __init__(self, main: MainInsurance, additional: AdditionalInsurance):
        self.main_insurance = main
        self.additional = additional

    @abstractmethod
    def __str__(self):
        pass

    def get_main_insurance(self):
        return self.main_insurance

    def get_additional_insurance(self):
        return self.additional


class HealthInsurancePackage(InsurancePackageFactory):
    def __init__(self):
        self.name = "Страхування здоров'я"
        super().__init__(HealthInsurance(), PetsInsurance())

    def __str__(self):
        description = "Страховий пакет <<Життєвий>> включає в себе:\n" \
                      "\t * "+str(self.main_insurance)+"\n" \
                      "\t * "+str(self.additional)+"\n"
        return description


class AutoInsurancePackage(InsurancePackageFactory):
    def __init__(self):
        self.name = "Страхування власності"
        super().__init__(CarInsurance(), BikeInsurance())

    def __str__(self):
        description = "Страховий пакет <<Безпека в дорозі>> включає в себе:\n" \
                      "\t * "+str(self.main_insurance)+"\n" \
                      "\t * "+str(self.additional)+"\n"
        return description


if __name__ == '__main__':
    human = HealthInsurancePackage()
    auto = AutoInsurancePackage()
    print(human)
    print()
    print(auto)




