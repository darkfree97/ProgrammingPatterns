# Шаблон проектування State ( Стан )
from abc import ABCMeta, abstractmethod
from enum import Enum
from random import randint

import time
import _thread


class HotLineState(metaclass=ABCMeta):
    @abstractmethod
    def request(self):
        pass


class ActiveMode(HotLineState):
    def __init__(self, parent):
        print("Set Active Mode")
        self.service = parent

    def request(self):
        if 8 <= self.service.time.localtime().tm_hour <= 13 or 14 < self.service.time.localtime().tm_hour <= 20:
            print("Check a free operator...")
            operator = None
            for op in self.service.operators:
                if op.status is OperatorStatus.AVAILABLE:
                    operator = op
                    operator.status = OperatorStatus.BUSY
                    break
            if operator is None:
                print("All operator busy!")
                self.service.state = WaitingMode(self.service)
                self.service.request()
            else:
                _thread.start_new_thread(operator.release, ())
                print(operator.get_answer())
        elif 13 < self.service.time.localtime().tm_hour <= 14:
            self.service.state = LunchMode(self.service)
            self.service.request()
        else:
            self.service.state = NightMode(self.service)
            self.service.request()


class WaitingMode(HotLineState):
    def __init__(self, parent):
        print("Set Waiting Mode")
        self.service = parent

    def request(self):
        print("Wait while some operator will be free!")
        time.sleep(5)
        self.service.state = ActiveMode(self.service)
        self.service.request()


class LunchMode(HotLineState):
    def __init__(self, parent):
        print("Set Lunch Mode")
        self.service = parent

    def request(self):
        if 13 < self.service.time.localtime().tm_hour <= 14:
            print(self.service.bot_sentences[randint(len(self.service.bot_sentences))])
        else:
            self.service.state = ActiveMode(self.service)
            self.service.request()


class NightMode(HotLineState):
    def __init__(self, parent):
        print("Set Night Mode")
        self.service = parent

    def request(self):
        if 8 > self.service.time.localtime().tm_hour or self.service.time.localtime().tm_hour > 20:
            print("Sorry we cannot give answer now ask as tomorrow!")
        else:
            self.service.state = ActiveMode(self.service)
            self.service.request()


class OperatorStatus(Enum):
    AVAILABLE = 1
    BUSY = 2


class Operator:
    def __init__(self, name):
        self.name = name
        self.status = OperatorStatus.AVAILABLE
        self.client_name = None

    def get_answer(self):
        return "Hello my name is "+self.name+" and i listen you."

    def release(self):
        time.sleep(15)
        self.status = OperatorStatus.AVAILABLE


class HotLineService:
    def __init__(self):
        self.operators = [Operator("Jessica"), Operator("Suzanna")]
        self.bot_sentences = ["Bot answer 1", "Bot answer 2", "Bot answer 3"]
        self.time = time
        self.state = ActiveMode(self)

    def request(self):
            self.state.request()


if __name__ == '__main__':
    service = HotLineService()
    service.request()
    service.request()
    service.request()
