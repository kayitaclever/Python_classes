
class Fruit:
    def __init__(self,name,Quantity,price):
        self.name=name
        self.Quantity=Quantity
        self.price=price


    def fruit_description(self):
        return(f"we have a store of {self.Quantity}  {self.name} at {self.price} each")

    def selling(self,sales):
        self.Quantity-=sales
        return (f"the stock is now {self.Quantity}")

    def purchasing(self,purchases):
        self.Quantity+=purchases
        return (f"the stock is now {self.Quantity}")    

    # def find_the_cheapest()    
