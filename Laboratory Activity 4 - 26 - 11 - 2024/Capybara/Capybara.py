class Capybara:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        gender_full = "Male" if self.gender.upper() == 'M' else "Female"
        return f"Name: {self.name}, Gender: {gender_full}, Age: {self.age} years old"
