from user import User

"""
This class built as Singleton style.
Creates our one and only SocialNetwork instance.
In addition responsible for sign up,sign in and log out.
"""


class SocialNetwork:
    __network = None
    users = []

    @staticmethod
    def __new__(cls, name):
        if not cls.__network:
            cls.__name__ = name
            cls.__network = super(SocialNetwork, cls).__new__(cls)
            print("The social network " + name + " was created!")
        return cls.__network

    @staticmethod
    def get_name():
        return SocialNetwork.__name__

    def sign_up(self, name, password):
        while name in self.users:
            print("Your name is at use, please enter a new name")
            name = input()

        while len(password) < 4 or len(password) > 8:
            print("please enter new password with at least 4 characters, at most 8 characters")
            password = input()
        user = User(name, password, True)
        self.users.append(user)
        return user

    def log_in(self, name, password):
        for user in self.users:
            if name == user.get_name() and password == user.get_password():
                user.online_flag = True
                print(str(user.get_name()) + " connected")

    def log_out(self, name):
        for user in self.users:
            if user.get_name() == name:
                user.online_flag = False
                print(user.get_name() + " disconnected")

    def __str__(self):
        user_info = "\n".join([user.__str__() for user in self.users])
        return f"{self.get_name()} social network:\n{user_info}"
