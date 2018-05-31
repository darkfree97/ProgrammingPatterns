# Шаблон проектування Strategy ( Стратегія )
"""
Стратегія — це поведінковий патерн проектування, 
який визначає сімейство схожих алгоритмів і розміщує 
кожен з них у власному класі. Після цього алгоритми можна 
заміняти один на інший прямо під час виконання програми.
"""
from abc import ABCMeta, abstractmethod
from reportlab.pdfgen import canvas


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, obj):
        pass


class PrintToPDFMethod(Strategy):
    def execute(self, obj):
        c = canvas.Canvas("files/strategy.pdf")
        c.drawString(150, 600, str(obj))
        c.save()


class PrintToTextFileMethod(Strategy):
    def execute(self, obj):
        file = open("files/strategy.txt", "w")
        file.write(str(obj))
        file.close()


class Context(metaclass=ABCMeta):
    @abstractmethod
    def set_strategy(self, strategy: Strategy):
        pass

    @abstractmethod
    def run_strategy(self):
        pass


class InsurancePolicy(Context):
    strategy_method = None

    def __init__(self, client, insurance):
        self.client = client
        self.insurance = insurance

    def set_strategy(self, strategy: Strategy):
        self.strategy_method = strategy

    def run_strategy(self):
        try:
            self.strategy_method.execute(self)
        except AttributeError:
            print("Strategy not set")

    def __str__(self):
        return "Insurance policy:\n\tClient - " + str(self.client) + "\n\tInsurance - " + str(self.insurance)


if __name__ == '__main__':
    policy = InsurancePolicy(input("Set client name ->"), input("Set insurance name ->"))
    policy.run_strategy()
    policy.set_strategy(PrintToPDFMethod())
    policy.run_strategy()
    policy.set_strategy(PrintToTextFileMethod())
    policy.run_strategy()
