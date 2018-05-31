# Шаблон проектування Singleton


# Функція декоратор яка використовується як функція обгортки для класів
def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


@singleton
class Clerk:
    name = None


if __name__ == '__main__':
    clerk1 = Clerk()
    clerk2 = Clerk()

    clerk1.name = "Ali"
    clerk2.name = "Mohamed"

    print("Name of clerk_1 is "+clerk1.name)
    print("Name of clerk_2 is "+clerk2.name)

