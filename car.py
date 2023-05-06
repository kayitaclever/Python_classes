
   
    
class Car:

    def __init__(self, make, model, year, speed):

        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        
    def describe_car(self):


        print(f"This is a {self.year} {self.make} {self.model} traveling at {self.speed} mph.")

    def accelerate(self,acceleration):

        self.speed+=acceleration
        return (f"my car is now travelling at {self.speed}")
    
    def deccelerate(self,decceleration):
        self.speed-=decceleration
        return (f"my car is now travelling at {self.speed}")



    
   