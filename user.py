from notify import Observer, Observable

"""
This class represents the user.
Notice that each user is observer and observable.
Hence this class inherited from Observable and from Observer.
This class also contains the factory method "publish_post"
publish_post responsible for sending each action(text,image,sell).
"""


class User(Observer, Observable):

    def __init__(self, name, password, online_flag):
        Observer.__init__(self)
        Observable.__init__(self)
        self.__name = name
        self.__password = password
        self.__online_flag = online_flag
        self.post = []

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def follow(self, u):
        if self.__online_flag:
            u.add_observer(self)
            print(str(self.__name) + " started following " + str(u.get_name()))

    def unfollow(self, u):
        if self.__online_flag:
            u.remove_observer(self)
            print(str(self.__name) + " unfollowed " + str(u.get_name()))

    def print_notifications(self):
        if self.__online_flag:
            print(self.get_name() + "'s notifications:")
            for notification in self.notification:
                print(notification)

    def __str__(self):
        return f"User name: {self.get_name()}, Number of posts: {len(self.post)}, Number of followers: {len(self.get_observers())}"

    """
    factory method.
    """

    def publish_post(self, *args):
        
        if not self.__online_flag: return
            
        from Post import TextPost, SalePost, ImagePost
        self.notify_observable(self.get_name() + " has a new post")

        if args[0] == "Text":
            p = TextPost(*args, self)
            self.post.append(p)
            return p
        elif args[0] == "Image":
            p = ImagePost(*args, self)
            self.post.append(p)
            return p
        elif args[0] == "Sale":
            p = SalePost(*args, self)
            self.post.append(p)
            return p
