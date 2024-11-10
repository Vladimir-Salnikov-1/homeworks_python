class User:

    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name

    def sayFname(self):
        print("Мое имя ", self.f_name)

    def sayLname(self):
        print("Моя фамилия ", self.l_name)

    def sayName(self):
        print("Меня зовут ", self.f_name, self.l_name)
