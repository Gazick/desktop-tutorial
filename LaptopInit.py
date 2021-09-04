class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'


laptop1 = Laptop('Asus', '18-bdfx', 37000)
laptop2 = Laptop('Samsung', '13-bsdf0xx', 47000)
