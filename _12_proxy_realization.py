# Шаблон проектування Заступник ( Proxy )
from sqlite3 import *
from abc import ABC, abstractmethod
import datetime


class DataBase(ABC):
    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_all(self):
        pass


class ClientDataBase(DataBase):
    def __init__(self):
        self.__db = connect(database="database")
        self.__cursor = self.__db.cursor()

    def update(self, *args, **kwargs):
        if len(args) == 3:
            self.__cursor.execute("UPDATE clients SET policy =? WHERE name=? AND surname=?", [args[2], args[0], args[1]])
            self.__db.commit()

    def create(self, *args, **kwargs):
        try:
            if len(args) == 2:
                self.__cursor.execute("INSERT INTO clients(name, surname) VALUES (?,?)", [args[0], args[1]])
                self.__db.commit()
        except IntegrityError:
            return "Client is already exist!!!"

    def get_all(self):
        self.__cursor.execute("SELECT * FROM clients")
        return [{"name": name, "surname": surname, "policy": policy} for (name, surname, policy) in self.__cursor]

    def delete(self, *args, **kwargs):
        if len(args) == 2:
            self.__cursor.execute("DELETE FROM clients WHERE name=? AND surname=?", [args[0], args[1]])
            self.__db.commit()
        elif len(kwargs) == 2:
            self.__cursor.execute("DELETE FROM clients WHERE name=? AND surname=?", [kwargs["name"], kwargs["surname"]])
            self.__db.commit()

    def __del__(self):
        self.__cursor.close()
        self.__db.close()


def log(message):
    v_log = open(file="log.txt", mode="a")
    v_log.write("["+str(datetime.datetime.now())+"] - "+message + "\n")
    v_log.close()


class ClientService(DataBase):
    def __init__(self):
        self.__db = None

    def prepare(self):
        if self.__db is None:
            self.__db = ClientDataBase()
            log("Database was connected!!!")

    def update(self, *args, **kwargs):
        self.prepare()
        self.__db.update(*args, **kwargs)
        log("Record of "+args[0]+" "+args[1]+" was changed. Additional parameter "+str(args[2]))

    def create(self, *args, **kwargs):
        self.prepare()
        self.__db.create(*args, **kwargs)
        log("Was added new record with name "+args[0]+" "+args[1])

    def get_all(self):
        self.prepare()
        log("Database return a set of clients")
        return self.__db.get_all()

    def delete(self, *args, **kwargs):
        self.prepare()
        self.__db.delete(*args, **kwargs)
        log("Was deleted a record with name " + args[0] + " " + args[1])

if __name__ == '__main__':
    db = ClientService()
    db.create("Kirimoshi", "Nara")
    db.update("Satoshi", "Nakamoto", 1)
    db.delete("Satoshi", "Nakamota")
    print(db.get_all())




