class Student:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_of_date(self):
        return self.date_of_birth

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth


stu1 = Student("Stu11", "Stu12", "1/1/1")
print(stu1.get_first_name(), stu1.get_last_name(), stu1.get_birth_of_date())
