class Zebra:

    def __init__(self, count=0):
        self.count = count

    def which_stripe(self):
        self.count += 1
        if self.count % 2 == 0:
            print("Полоска черная")
        else:
            print("Полоска белая")


z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
z2.which_stripe()