# Шаблон проектування Будівельник ( Builder )
from abc import ABC, abstractmethod


class InsurancePolicy:
    main_insurance = None
    additional_insurance = None
    client = None

    def set_client(self, client):
        self.client = client

    def __str__(self):
        return "Даний страховий поліс включає:" \
               "\n\t- "+str(self.main_insurance) + \
               "\n\t- "+str(self.additional_insurance) + \
               "\nДля клієнта ( "+str(self.client)+" )"


class InsurancePolicyBuilder(ABC):
    def __init__(self, policy=InsurancePolicy()):
        self.insurance_policy = policy

    def reset(self, policy=InsurancePolicy()):
        self.insurance_policy = policy

    def get_result(self):
        return self.insurance_policy

    @abstractmethod
    def build_main_insurance(self):
        pass

    @abstractmethod
    def build_addition_insurance(self):
        pass


class HealthInsurancePolicyBuilder(InsurancePolicyBuilder):
    def build_main_insurance(self):
        self.insurance_policy.main_insurance = "Страхування життя"

    def build_addition_insurance(self):
        self.insurance_policy.additional_insurance = "Страхування життя домашнього улюбленця"


class PropertyInsurancePolicyBuilder(InsurancePolicyBuilder):
    def build_main_insurance(self):
        self.insurance_policy.main_insurance = "Страхування автомобіля"

    def build_addition_insurance(self):
        self.insurance_policy.additional_insurance = "Страхування мотоцикла"


class Clerk:
    __insurance_policy_builder = None

    def set_insurance_policy_builder(self, builder: InsurancePolicyBuilder):
        self.__insurance_policy_builder = builder

    def create_insurance_policy(self):
        self.__insurance_policy_builder.build_main_insurance()
        self.__insurance_policy_builder.build_addition_insurance()
        return self.__insurance_policy_builder.insurance_policy

    def get_insurance_policy(self):
        return self.__insurance_policy_builder.insurance_policy

if __name__ == '__main__':
    b1 = HealthInsurancePolicyBuilder()
    b2 = PropertyInsurancePolicyBuilder()

    clerk = Clerk()
    clerk.set_insurance_policy_builder(b1)
    clerk.create_insurance_policy()
    policy1 = clerk.get_insurance_policy()
    policy1.set_client("Юрій Гагарін")
    print(policy1)

    clerk.set_insurance_policy_builder(b2)
    clerk.create_insurance_policy()
    policy2 = clerk.get_insurance_policy()
    policy2.set_client("Леонід Каденюк")
    print(policy2)


