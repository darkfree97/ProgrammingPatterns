import _4_builder_realisation
from abc import ABC, abstractmethod


class Tariff:
    cost = 0
    period = "Період не встановлений"

    @abstractmethod
    def __str__(self):
        pass


class Premium(Tariff):
    def __init__(self):
        self.cost = 300
        self.period = "1 рік"

    def __str__(self):
        return "Преміум тариф"


class Extra(Tariff):
    def __init__(self):
        self.cost = 100
        self.period = "6 міс."

    def __str__(self):
        return "Преміум тариф"


class InsurancePolicy(_4_builder_realisation.InsurancePolicy):
    tariff = None

    def __init__(self, main, addition, tariff: Tariff, client):
        self.main_insurance = main
        self.additional_insurance = addition
        self.tariff = tariff
        self.client = client

    @abstractmethod
    def __str__(self):
        pass


class HealthInsurancePolicy(InsurancePolicy):
    def __init__(self, tariff: Tariff, client):
        super().__init__("Страхування життя", "Страхування домашнього улюбленця", tariff, client)
        self.name = "Страховий поліс 'Живий'"

    def __str__(self):
        return self.name+" - " + _4_builder_realisation.InsurancePolicy.__str__(self) + "\n" + str(self.tariff)


class PropertyInsurancePolicy(InsurancePolicy):
    def __init__(self, tariff: Tariff, client):
        super().__init__("Страхування дому", "Страхування автомобіля", tariff, client)
        self.name = "Страховий поліс 'Безпека власності'"

    def __str__(self):
        return self.name+" - " + _4_builder_realisation.InsurancePolicy.__str__(self) + "\n" + str(self.tariff)


if __name__ == '__main__':
    policy = HealthInsurancePolicy(Premium(), "Гагарін")
    print(policy)

