# Шаблон проектування Object Pool ( Пул об'єктів )
from random import randint
from _5_singleton_realization import singleton


class AiAssistant:
    def __init__(self, messages: tuple):
        self.messages = messages

    def generate_answer(self):
        return self.messages[randint(0, len(self.messages)-1)]


class HelloAiAssistant(AiAssistant):
    def __init__(self):
        super().__init__(("Hi", "Hello", "Good afternoon"))


class ByeAiAssistant(AiAssistant):
    def __init__(self):
        super().__init__(("Bye", "Hello", "Good Bye"))


@singleton
class Pool:
    def __init__(self):
        self.objects = {HelloAiAssistant: HelloAiAssistant(), ByeAiAssistant: ByeAiAssistant()}

    def __getitem__(self, item):
        return self.objects.get(item)


if __name__ == '__main__':
    pool = Pool()
    print(pool[HelloAiAssistant].generate_answer())
    print(pool[ByeAiAssistant].generate_answer())
