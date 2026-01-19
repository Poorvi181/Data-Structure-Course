class Car:
    def __init__(self,color,brand,model):
        self.color=color
        self.brand=brand
        self.model=model

    def Start(self):
        print("Car Started")

    def Stop(self):
        print("Car Stopped")

    def display_details(self):
        print("Car Details: ")
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Color: ", self.color)

mycar = Car ("Blue", "Tesla", "Long Range")

mycar.display_details()
mycar.Start()
mycar.stop()