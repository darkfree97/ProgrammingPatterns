# Шаблон пректування Mediator ( Посередник )
from abc import ABCMeta, abstractmethod
import _thread
from time import sleep


class View(metaclass=ABCMeta):
    @abstractmethod
    def update(self, content):
        pass


class UserView(View):
    def __init__(self, username: str):
        self.username = username
        self.displaying_messages = []

    def new_message(self, message):
        self.displaying_messages.append((self.username, message))

    def update(self, content):
        self.displaying_messages = content


class ServiceBot(metaclass=ABCMeta):
    @abstractmethod
    def if_has_message(self):
        pass


class UserResponseServiceBot(ServiceBot):
    def __init__(self):
        self.message_count = 0
        self.user_views = [UserView("Clinton"), UserView("Lincoln")]
        self.temp_new_message = None
        _thread.start_new_thread(self.if_has_message, ())

    def if_has_message(self):
        while True:
            for view in self.user_views:
                c = len(view.displaying_messages)
                if c > self.message_count:
                    self.message_count = c
                    self.temp_new_message = view.displaying_messages
                    print("__________________________")
                    print(str(self.temp_new_message))
                    break
            for view in self.user_views:
                view.update(self.temp_new_message)
            sleep(2)


if __name__ == '__main__':
    bot = UserResponseServiceBot()
    bot.user_views[0].new_message("Hello World")
    sleep(1)
    bot.user_views[1].new_message("Good Bye")
    input()
