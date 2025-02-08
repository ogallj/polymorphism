class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Private attribute (Encapsulation)

    def get_price(self):
        """Getter method to access private price"""
        return self.__price

    def set_price(self, new_price):
        """Setter method to modify price"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

    def display_info(self):
        print(f"Smartphone: {self.brand} {self.model}, Price: ${self.__price}")

# Subclass with inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, refresh_rate):
        super().__init__(brand, model, price)
        self.refresh_rate = refresh_rate  # Additional attribute

    def display_info(self):
        """Override method to include refresh rate"""
        super().display_info()
        print(f"Refresh Rate: {self.refresh_rate}Hz (Great for gaming!)")

# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", 999)
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 1299, 144)

phone1.display_info()
gaming_phone.display_info()
