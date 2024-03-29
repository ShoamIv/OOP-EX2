"""
notify class, contains two classes:
Observable and Observer classes that maintain subscribes for posts and followers.
for every subscriber notifies them automatically of any state changes.
"""


class Observable:
    def __init__(self):
        self.__observers = []

    def get_observers(self):
        return self.__observers

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observable(self, info):
        for observer in self.__observers:
            observer.update(info)


class Observer:

    def __init__(self):
        self.notification = []

    def update(self, info):
        self.notification.append(info)
