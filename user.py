from notify import Observer, Observable


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
            self.add_observer(u)

    def unfollow(self, u):
        if self.__online_flag:
            self.remove_observer(u)

    def print_notifications(self):
        if self.__online_flag:
            for notification in self.notification:
                print(notification)

    def __str__(self):
        return f"User name: {self.get_name()}, Number of posts: {len(self.post)}, Number of followers: {len(self.get_observers())}"

    #
    # factory methood
    #
    def publish_post(self, *args):
        from Post import TextPost, SalePost, ImagePost
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
