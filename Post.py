import matplotlib.pyplot as plt

import user
from notify import Observable
from user import User


class Post(Observable):

    def __init__(self, type_of, info, u):
        super().__init__()
        self.type_of = type_of
        self.u = u
        self.info = info
        self.add_observer(u)

    def like(self, u):
        if self.u.get_name == u.get_name:
            return False
        info = "notification to "+self.u.get_name()+": " + u.get_name() + " liked your post"
        self.notify_observable(info)

    def comment(self, u, commented):
        if self.u.get_name == u.get_name:
            return False
        self.notify_observable("notification to "+self.u.get_name()+": " + u.get_name() + " commented on your post: " + commented)


class TextPost(Post):

    def __init__(self, type_of, info, u):
        super().__init__(type_of, info, u)
        print(u.get_name() + " published a post:\n" + info)

    def __str__(self):
        return self.u.get_name() + " published a post:\n" + self.info


class ImagePost(Post):

    def __init__(self, type_of, image_url, u):
        super().__init__(type_of, image_url, u)
        print(u.get_name() + " posted a picture")

    def __str__(self):
        return self.u.get_name() + " posted a picture:\n" + self.info

    def display(self):
        plt.show()


class SalePost(Post):
    def __init__(self, type_of, car_info, sale_price, location, user):
        super().__init__(type_of, car_info, user)
        self.sale_price = sale_price
        self.location = location

    def discount(self, discount, password):
        if self.u.get_password() == password:
            self.sale_price -= self.sale_price * (discount / 100)
            print("Discount on " + self.u.get_name() + " product! the new price is: " + str(self.sale_price))

    def sold(self, password):
        if self.u.get_password() == password:
            print(self.u.get_name() + " product is sold")
            self.info = "Sold! " + str(self.info)

    def __str__(self):
        return "Discount on " + self.u.get_name() + " product! the new price is:" + str(self.sale_price)
