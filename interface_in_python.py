from abc import ABCMeta
from abc import abstractmethod

class interface1(metaclass=ABCMeta):
    @abstractmethod
    def status(self):
        pass

class Car(interface1):
    def __init__(self):
        pass
    def status():
        print("some status")
    
si = Car()
