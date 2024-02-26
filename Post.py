import matplotlib.pyplot as plt
import matplotlib.image as img
import user
from notify import Observable
from user import User

"""
Post class, which allows users to post text,images and items for sale.
Notice that post inherited from Observable.
Post is a Subject to User.
"""


class Post(Observable):

    def __init__(self, type_of, info, u: 'User'):
        super().__init__()
        self.type_of = type_of
        self.u = u
        self.info = info
        self.add_observer(u)

    def like(self, u_s: User):
        if self.u.get_name == u_s.get_name:
            return False
        print(f"notification to {self.u.get_name()}: {u_s.get_name()} liked your post")
        self.notify_observable(f"{u_s.get_name()} liked your post")

    def comment(self, u_s, commented):
        if self.u.get_name == u_s.get_name:
            return False
        print(f"notification to {self.u.get_name()}: {u_s.get_name()} commented on your post: {commented}")
        self.notify_observable(f"{u_s.get_name()} commented on your post")


class TextPost(Post):

    def __init__(self, type_of, info, u):
        super().__init__(type_of, info, u)
        print(u.get_name() + " published a post:\n" + '"' + info + '"'+'\n')

    def __str__(self):
        return self.u.get_name() + " published a post:\n" + '"' + self.info + '"'"\n"


class ImagePost(Post):

    def __init__(self, type_of, image_url, u):
        super().__init__(type_of, image_url, u)
        print(u.get_name() + " posted a picture")

    def display(self):
        image = img.imread(self.info)
        plt.imshow(image)
        print("Shows picture")

    def __str__(self):
        return self.u.get_name() + " posted a picture\n"


class SalePost(Post):
    def __init__(self, type_of, car_info, sale_price, location, u_s):
        super().__init__(type_of, car_info, u_s)
        self.sale_price = sale_price
        self.location = location
        self.sell = "For sale!"

        print(f"{self.u.get_name()} posted a product for sale:")
        print(f"{self.sell} {self.info}, price: {self.sale_price}, pickup from: {self.location}\n")

    def discount(self, discount, password):
        if self.u.get_password() == password:
            self.sale_price -= self.sale_price * (discount / 100)
            print(f"Discount on {self.u.get_name()} product! the new price is: {self.sale_price}")

    def sold(self, password):
        if self.u.get_password() == password:
            print(f"{self.u.get_name()}'s product is sold")
            self.sell = "Sold!"

    def __str__(self):
        return f"{self.u.get_name()} posted a product for sale:\n{self.sell} {self.info}, price: {self.sale_price}, pickup from: {self.location}"
