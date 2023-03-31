class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_cats(self):
        return f"Имя: {self.name}, пол: {self.gender}, возраст: {self.age}"
