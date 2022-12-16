
class Product:
   product_name = ''
   product_price = 0
   product_category = ''
   def __init__(self, product_name, product_price, product_category):
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category

my_favorite = Product('Apple', 3, "Fruit")
print(my_favorite.product_price)
my_favorite.print(Product)