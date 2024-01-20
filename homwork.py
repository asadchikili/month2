from abc import ABC, abstractmethod

class GeeksPeople(ABC):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    @abstractmethod
    def __str__(self):
        pass
class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study
    def study(self):
        return f"{self.name} is studying in group {self.group_where_study}"
    def __str__(self):
        return f"Student:\n{super().__str__()}\nStudent ID: {self.student_id}\nGroup: {self.group_where_study}"
class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        super().__init__(name, email, phone)
        self.teacher_id = teacher_id
    def teach(self):
        return f"{self.name}  {self.group_where_teach}"
    def __str__(self):
        return f"Teacher:\n{super().__str__()}\nTeacher ID: {self.teacher_id} {self.group_where_teach}"
class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        super().__init__(name, email, phone)
        self.admin_id = admin_id
    def create_group(self, group_name):
        return f" {self.name}  {group_name}"
    def __str__(self):
        return f"Admin:\n{super().__str__()}\nAdmin ID: {self.admin_id}"
student1 = Student("John Doe", "john@example.com", "123-456-7890", "S12345", "Group A")
print(student1)
from abc import ABC, abstractmethod

class GeeksPeople(ABC):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    @abstractmethod
    def __str__(self):
        pass
class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        super().__init__(name, email, phone)
        self.student_id = student_id
    def study(self):
        return f"{self.name} is studying in group {self.group_where_study}"
    def __str__(self):
        return f"Student:\n{super().__str__()}\nStudent ID: {self.student_id}\nGroup: {self.group_where_study}"
class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        super().__init__(name, email, phone)
        self.teacher_id = teacher_id
    def teach(self):
        return f"{self.name} is teaching in group {self.group_where_teach}"
    def __str__(self):
        return f"Teacher:\n{super().__str__()}\nTeacher ID: {self.teacher_id}\nTeaching Group: {self.group_where_teach}"
class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        super().__init__(name, email, phone)
        self.admin_id = admin_id
    def create_group(self, group_name):
        return f"Admin {self.name} created a new group: {group_name}"
    def __str__():
        return f"Admin:\n{super().__str__()}\nAdmin ID: {self.admin_id}"
teacher1 = Teacher("Js", "js@example.com", "987-654-3210", "T98765", "Group B")
admin1 = Admin("As", "as@example.com", "555-555-5555", "A001")
print(teacher1)
print(teacher1.teach())
print(" + "-"*30 + ")
print(admin1)


class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id,):
        Student.__init__(self, name, email, phone, student_id, )
        Teacher.__init__(self, name, email, phone, teacher_id, )
    def __str__(self):
        return f"Mentor:\n{super().__str__()}\nMentor has properties from both Student and Teacher"
mentor1 = Mentor("Mentor menotovr", "mentor@example.com", "111-222-3333", "S67890", "Group C", "T54321", "Group D")
print(mentor1)

