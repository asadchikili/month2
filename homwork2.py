
class Person:
    def __init__(self, fullname, age, married):
        self.fullname = fullname
        self.age = age
        self.married = married
    def introduce_myself(self):
        marital_status = "женат(замужем)" if self.married else "не женат(не замужем)"
        print(f"Привет, меня зовут {self.fullname}, мне {self.age} лет. Я {marital_status}.")
person1 = Person("Иван Иванов", 30, False)
person2 = Person("Мария Петрова", 25, True)
person1.introduce_myself()
person2.introduce_myself()

# class Teacher(Person):
#     def __init__(self, fullname, age, married, experience):
#         super().__init__(fullname, age, married)
#         self.experience = experience
#     def introduce_myself(self):
#         marital_status = "женат(замужем)" if self.married else "не женат(не замужем)"
#         print(f"Привет, меня зовут {self.fullname}, мне {self.age} лет. Я {marital_status}. Опыт работы: {self.experience} лет.")
# person1 = Person("Иван Иванов", 30, False)
# teacher1 = Teacher("Анна Сидорова", 35, True, 10)
# person1.introduce_myself()
# teacher1.introduce_myself()


class Teacher(Person):
    salary_base = 50000

    def __init__(self, fullname, age, married, experience):
        super().__init__(fullname, age, married)
        self.experience = experience
        self.salary = self.calculate_salary()

    def calculate_salary(self):
        bonus_per_year = 3000
        return self.salary_base + (self.experience * bonus_per_year)

    def introduce_myself(self):
        marital_status = "женат(замужем)" if self.married else "не женат(не замужем)"
        print(f"Привет, меня зовут {self.fullname}, мне {self.age} лет. Я {marital_status}. Опыт работы: {self.experience} лет. Зарплата: {self.salary}.")

teacher = Teacher("Асадбек", 39, True, 10)
teacher.introduce_myself()
