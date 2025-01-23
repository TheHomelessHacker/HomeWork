class Student():
    def __init__(self, nameStudent, surnameStudent, genderStudent):
        self.__name = nameStudent
        self.__surname = surnameStudent
        self.__gender = genderStudent
        '''инициализируем этот атрибут для каждого экземпляра по отдельности и у каждого студента будут свои пройденные курсы.'''
        self.__finishedCourses = []
        self.__grades = {}
        self.__coursesInProgress = []

    def getNameStudent(self):
        return self.__name

    def getSurnameStudent(self):
        return self.__surname

    def getGender(self):
        return self.__gender

    def getFinishedCourses(self):
        return self.__finishedCourses

    def getGrades(self):
        return self.__grades

    def getCoursesInProgress(self):
        return self.__coursesInProgress

    '''-------------------------------------------------'''

    def setNameStudent(self, name):
        self.__name = name

    def setSurnameStudent(self, surname):
        self.__surname = surname

    def setGender(self, gender):
        self.__gender = gender

    def setFinishedCourses(self, finishedCourses):
        self.__finishedCourses.extend(finishedCourses)

    def setGrades(self, grades):
        self.__grades.update(grades)

    def setCoursesInProgress(self, coursesInProgress):
        self.__coursesInProgress.append(coursesInProgress)

    def __str__(self):
        return f"Студент {self.__name} {self.__surname}, {self.__gender}"


class Mentor:
    def __init__(self, nameMentor, surnameMentor):
        self.__name = nameMentor
        self.__surname = surnameMentor
        self.__courses_attached = []
    
    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname
    
    def getCoursesAttached(self):
        return self.__courses_attached

    def setName(self, name):
        self.__name = name
    
    def setSurname(self, surname):
        self.__surname = surname

    def setCoursesAttached(self, coursesAttached):
        self.__courses_attached.append(coursesAttached)

    # функция взаимодействия сдунтов с преподавателем 
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.__courses_attached and course in student.getCoursesInProgress():
            if course in student.getGrades():
                student.getGrades()[course] += [grade]
            else:
                student.getGrades()[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Преподаватель {self.__name} {self.__surname}"
    
class Lecturer(Mentor):
    def __init__(self, nameMentor, surnameMentor):
        super().__init__(nameMentor, surnameMentor)

class Reviewer(Mentor):
    def __init__(self, nameMentor, surnameMentor):
        super().__init__(nameMentor, surnameMentor)


student1 = Student('Mark', 'Zdorovets', 'man')
# ? как праильно реализовать добавление може быть 1 или срузу несколько
student1.setCoursesInProgress("OOP")
# ? как праильно реализовать добавление може быть 1 или срузу несколько
student1.setFinishedCourses(['Python', 'Git'])
student1.setGrades({'Python': [10, 10, 10]})
student1.setGrades({'Git': [10, 10, 10]})

print(list(map(lambda x: x+1, [1,2,3])))

print(student1)
print(f"Занимается {student1.getCoursesInProgress()}")
print(f"Закончил {student1.getFinishedCourses()}")
print(f"Получил оценки {student1.getGrades()}")


mentor1 = Mentor("Павел", "Молибог")
mentor1.setCoursesAttached("OOP")

print(mentor1)
print(f"Преподаёт {mentor1.getCoursesAttached()}")


# Ставим оценки ученику
mentor1.rate_hw(student1, "OOP", 10)
mentor1.rate_hw(student1, "OOP", 10)
mentor1.rate_hw(student1, "OOP", 10)
mentor1.rate_hw(student1, "OOP", 1)

print(student1.getGrades())