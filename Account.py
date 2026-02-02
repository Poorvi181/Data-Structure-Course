class User:
    __password = "Abc@123"

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username

    def getPassword(self):
        return self.__password
    
    def setPassword(self):
        old_password = input("Enter your old password: ")

        if old_password == self.__password:
            new_password = input("Enter your new password: ")
            self.__password = new_password
            print("New Password Creation Is Successful.")
            print("New password is:", new_password)

        else:
            print("Please enter correct password.")

poorvi = User("Poorvi Ahlawat", "poorvi.jetlearn@gmail.com", "poorvi_ahlawat")
print(poorvi.name)
print(poorvi.getPassword())
poorvi.setPassword()

class Car:
    def __init__(self, brand, model, fuel, color):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.color = color

    def getColor(self):
        return self.color
    
    def setColor(self, newcolor):
        self.color = newcolor

    def showCar(self):
        print("Car - {} - {}. Fuel Type - {}, color - {}".format(
            self.brand, self.model, self.fuel, self.color
        ))

class SUV(Car):
    def __init__(self, brand, model, fuel, color, transmission, turbo):
        Car.__init__(self, brand, model, fuel, color)
        self.transmission = transmission
        self.turbo = turbo
    def showCar(self):
        print(
            "Car - {} - {}. Fuel Type - {}, Color - {}, Transmission - {}, Turbo True/False - {}".format(
                self.brand,
                self.model,
                self.fuel,
                self.color, 
                self.transmission,
                self.turbo

            )
        )

audiQ3 = SUV("Audi", "Q3", "Diesel", "White", "Auto", True)
print(audiQ3.getColor())
audiQ3.setColor("Red")
audiQ3.showCar()