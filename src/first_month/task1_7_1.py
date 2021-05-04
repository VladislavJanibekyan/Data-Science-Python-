class Person():
    def __init__(self,name,surname,age,gender):
        self.__name = name
        self.__surname = surname 
        self.__age = age
        self.__gender = gender
    def __repr__(self):
        return f" - {self.__name} {self.__surname} - {self.__gender}, {self.__age} years old"


class Student(Person):
    def __init__(self,name,surname,age,gender,university,faculty,course,middle_score):
        super().__init__(name,surname,age,gender)
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__middle_score = middle_score
    def __repr__(self):
        super().__repr__()
        return f"{self.__university}-{self.__faculty}-{self.__course}-{self.__middle_score}"

    def get_score(self):
        return self.__middle_score
    def set_score(self,middle_score):
        self.__middle_score = middle_score
    def del_score(self):
        del self.__middle_score
    middle_score = property(get_score,set_score,del_score,doc="esim")

    def get_course(self):
        return self.__course
    def set_course(self,course):
        self.__course = course
    def del_course(self):
        del self.__course
    course = property(get_course,set_course,del_course,doc="esim")

    def get_faculty(self):
        return self.__faculty
    def set_faculty(self,faculty):
        self.__faculty = faculty
    def del_faculty(self):
        del self.__faculty
    faculty = property(get_faculty,set_faculty,del_faculty,doc="esim")

    def get_university(self):
        return self.__university
    def set_univeristy(self,university):
        self.__university = university
    def del_university(self):
        del self.__university
    university = property(get_university,set_univeristy,del_university,doc="esim")



class Teacher(Person):
    def __init__(self,name,surname,age,gender,university,faculty,discipline,experience,salary):
        super().__init__(name,surname,age,gender)
        self.__university = university
        self.__faculty = faculty
        self.__discipline = discipline
        self.__experience = experience
        self.__salary = salary
    def __repr__(self):
        super().__repr__()
        return f"{self.__university}-{self.__faculty}-{self.__discipline}-{self.__experience}-{self.__salary}"

    def get_university(self):
        return self.__university
    def set_univeristy(self,university):
        self.__university = university
    def del_university(self):
        del self.__university
    university = property(get_university,set_univeristy,del_university,doc="esim")

    def get_faculty(self):
        return self.__faculty
    def set_faculty(self,faculty):
        self.__faculty = faculty
    def del_faculty(self):
        del self.__faculty
    faculty = property(get_faculty,set_faculty,del_faculty,doc="esim")

    def get_discipline(self):
        return self.__discipline
    def set_discipline(self,discipline):
        self.discipline = discipline
    def del_discipline(self):
        del self.discipline
    discipline = property(get_discipline,set_discipline,del_discipline,doc="esim")

    def get_experience(self):
        return self.__experience
    def set_experince(self,experience):
        self.experience = experience
    def del_experince(self):
        del self.experience
    experience = property(get_experience,set_experince,del_experince,doc="esim")
    
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        self.salary = salary
    def del_salary(self):
        del self.salary
    salary = property(get_salary,set_salary,del_salary,doc="esim")

a = Teacher("vahag","hovakimyan",34,"male","usi","politic","plsi",4,34000)
a = Student("karen","davtyan",26,"male","ysu","pol",3,4)

print(a, a.university)

