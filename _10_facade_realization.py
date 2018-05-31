# Шаблон проектування Фасад ( Facade )
from _2_abstract_factory_realization import *
from _9_decorator_realization import *
from _12_proxy_realization import ClientService


class InsurancePolicyExtended(Document):
    def __init__(self):
        self.__policy = None

    def set_policy(self, policy: InsurancePackageFactory):
        self.__policy = policy

    def show_info(self):
        print(self.__policy)


class User:
    def __init__(self, surname: str, name: str):
        self.surname = surname
        self.name = name

    def __str__(self):
        return self.name+" "+self.surname


class Controller:
    def __init__(self):
        self.__service = None
        self.__policy = InsurancePolicyExtended()
        self.__agreement = Agreement(self.__policy)
        self.__insurance_polices = []
        self.__insurance_polices.append(HealthInsurancePackage())
        self.__insurance_polices.append(AutoInsurancePackage())
        self.__users = {}

    def __add_user(self, user: User):
        self.__users[user] = None

    def __set_insurance_for_user(self, user_index, ins_index):
        user = list(self.__users.keys())[user_index]
        self.__users[user] = ins_index

    def __add_insurance_for_new_user(self, user: User, insurance_index):
        self.__users[user] = insurance_index

    def __print_all_agreements(self):
        for user in self.__users:
            if self.__users[user] is not None:
                print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>")
                self.__policy.set_policy(self.__insurance_polices[int(self.__users[user])])
                self.__agreement.set_client(user)
                self.__agreement.show_info()

    def control(self):
        while True:
            cmd = input("MENU:\n"
                        "1 - add user\n"
                        "2 - add user and change policy\n"
                        "3 - change user policy\n"
                        "4 - print all agreements\n>")
            if cmd == "1":
                surname = input("Input surname of new User: ")
                name = input("Input name of new User: ")
                self.__add_user(User(surname, name))
            elif cmd == "2":
                surname = input("Input surname of new User: ")
                name = input("Input name of new User: ")
                print("Select a insurance:")
                while True:
                    for index, item in enumerate(self.__insurance_polices):
                        print("  " + str(item) + " - " + str(index))
                    insurance_index = int(input("Input index of policy ->"))
                    if insurance_index < len(self.__insurance_polices):
                        break
                    else:
                        print("\033[31m" + "Wrong index. Please Try again." + "\033[0m")
                self.__add_insurance_for_new_user(User(surname, name), insurance_index)
            elif cmd == "3":
                print("Select a user:")
                while True:
                    for index, item in enumerate(self.__users.keys()):
                        print((u' \u2717' if self.__users[item] is None else u' \u2713')
                              + "  " + str(item) + " - " + str(index))
                    user_index = int(input("Input index of user ->"))
                    if user_index < len(self.__users):
                        break
                    else:
                        print("\033[31m " + "Wrong index. Please Try again." + "\033[0m")

                print("Select a insurance:")
                while True:
                    for index, item in enumerate(self.__insurance_polices):
                        print("  "+str(item) + " - " + str(index))
                    insurance_index = int(input("Input index of policy ->"))
                    if insurance_index < len(self.__insurance_polices):
                        break
                    else:
                        print("\033[31m" + "Wrong index. Please Try again." + "\033[0m")
                self.__set_insurance_for_user(user_index, insurance_index)
            elif cmd == "4":
                self.__print_all_agreements()
            else:
                break

    def test(self):
        self.__service = ClientService()
        for item in self.__service.get_all():
            if item["policy"] is None:
                self.__add_user(User(item["surname"], item["name"]))
            else:
                self.__add_insurance_for_new_user(User(item["surname"], item["name"]), item["policy"])


if __name__ == '__main__':
    controller = Controller()
    controller.test()
    controller.control()


