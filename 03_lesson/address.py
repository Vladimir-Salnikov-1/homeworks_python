class Address:

    def __init__(self, index, city, street, house, kvartira):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.kvartira = kvartira

    def __str__(self):
        return f"""{self.index}, {self.city}, {self.street}, {self.house},
                 {self.kvartira}"""
