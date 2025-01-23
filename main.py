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

    # ! попробовать через map написать
    def getAvarageGrade(self):
        a = 0
        len_ = 0
        for grade in self.__grades.values():
            a += sum(grade)
            len_ += len(grade)
        return a / len_
    
    def getFinishCourses(self):
        s = ''
        for course in self.__finishedCourses:
            s += course + ', '
        s = s.rstrip(", ")
        return s

    def getInProgressCourses(self):
        s = ''
        for course in self.__coursesInProgress:
            s += course + ', '

        s = s.rstrip(", ")
        return s

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

    # ? не очень понимаю как правильно обработать grade > 10
    def EvaluationOfTheLecturerWork(self, lecturer, course, grade):
        if grade <= 10:
            if isinstance(lecturer, Lecturer) and course in lecturer.getCoursesAttached() and course in self.getCoursesInProgress():
                if course in lecturer.getGrades():
                    lecturer.getGrades()[course] += [grade]
                else:
                    lecturer.getGrades()[course] = [grade]
            else:
                return f"Лектор {lecturer.getName} не прикреплён к курсу {course}"
        else:
            return "У нас 10-ти бальная система оценивания!"
        
    def ComparisonOfStudents(self, student2):
        if self.getAvarageGrade() > student2.getAvarageGrade():
            return f"Лучше оказался студент {self.getNameStudent()} со средним баллом {self.getAvarageGrade()}"
        elif self.getAvarageGrade() < student2.getAvarageGrade():
            return f"Лучше оказался студент {student2.getNameStudent()} со средним баллом {self.getAvarageGrade()}"
        else:
            return f"студенты {self.getNameStudent()} и {student2.getNameStudent()} имеют одинаковый средний балл {self.getAvarageGrade()}"

    def __str__(self):
        print()
        return f"Имя: {self.__name}\n\
Фамилия: {self.__surname}\n\
Средняя оценка за домашние задания: {self.getAvarageGrade()}\n\
Курсы в процессе изучения: {self.getInProgressCourses()}\n\
Завершенные курсы: {self.getFinishCourses()}"

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
    
    def __str__(self):
        return f"Преподаватель {self.__name} {self.__surname}"
    
class Lecturer(Mentor):
    def __init__(self, nameMentor, surnameMentor):
        super().__init__(nameMentor, surnameMentor)
        self.__courses_attached = []
        self.__grades = {}

    def getCoursesAttached(self):
        if self.__courses_attached == []:
            return f"Лектор {self.getName()} не закреплён ни за одним курсом"
        else:
            return f"Вот курсы - {self.__courses_attached} за которыми закреплён преподаватель {self.getName()}" 
        # return self.__courses_attached

    def getGrades(self):
        return self.__grades

    def setCoursesAttached(self, coursesAttached):
        self.__courses_attached.append(coursesAttached)

    def setGrades(self, grades):
        self.__grades.update(grades)

    def getAvarageGrade(self):
        a = 0
        len_ = 0
        for grade in self.__grades.values():
            a += sum(grade)
            len_ += len(grade)
        return a / len_

    def ComparisonOfLecturers(self, lecturer2):
        if self.getAvarageGrade() > lecturer2.getAvarageGrade():
            return f"Лучше оказался преподавтель {self.getName()}"
        elif self.getAvarageGrade() < lecturer2.getAvarageGrade():
            return f"Лучше оказался преподавтель {lecturer2.getName()}"
        else:
            return f"Преподаватели {self.getName()} и {lecturer2.getName()} получили от студентов одинаковые оценки"    

    def __str__(self):
        return f"Имя: {self.getName()}\n\
Фамилия: {self.getSurname()}\n\
Средняя оценка за лекции: {self.getAvarageGrade()}"

class Reviewer(Mentor):
    def __init__(self, nameMentor, surnameMentor):
        super().__init__(nameMentor, surnameMentor)
        self.__courses_attached = []

    def getCoursesAttached(self):
        return f"Reviewer {self.getName()} закреплен за курсами:{self.__courses_attached}"

    def setCoursesAttached(self, coursesAttached):
        self.__courses_attached.append(coursesAttached)

    def AssessmentOfStudentWork(self, student, course, grade):
        if isinstance(student, Student) and course in self.__courses_attached and course in student.getCoursesInProgress():
            if course in student.getGrades():
                student.getGrades()[course] += [grade]
            else:
                student.getGrades()[course] = [grade]
            print(f"Преподаватель {self.getName()} поставил оценку {grade} студенту {student.getNameStudent()} по теме {course}")
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.getName()}\n\
Фамилия: {self.getSurname()}"

student1 = Student('Mark', 'Zdorovets', 'man')
# ? как праильно реализовать добавление може быть 1 или срузу несколько
student1.setCoursesInProgress("OOP")
# ? как праильно реализовать добавление може быть 1 или срузу несколько
student1.setFinishedCourses(['Python', 'Git'])
student1.setGrades({'Python': [10, 10, 10]})
student1.setGrades({'Git': [10, 10, 10]})

student2 = Student("Elon", "Mask", "robot")
student2.setGrades({'Python': [9, 9, 9]})

print(student1)
# print(f"Занимается {student1.getCoursesInProgress()}")
# print(f"Закончил {student1.getFinishedCourses()}")
# print(f"Получил оценки {student1.getGrades()}")
# print(student1.getAvarageGrade())
print(student1.ComparisonOfStudents(student2))
print()

lecturer1 = Lecturer("Peta", "W")
lecturer1.setCoursesAttached("OOP")
# print(lecturer1.getCoursesAttached())
student1.EvaluationOfTheLecturerWork(lecturer1, "OOP", 10)
print(lecturer1)
# print(lecturer1.getGrades())
print()

lecturer2 = Lecturer("Anna", "K")
lecturer2.setCoursesAttached("OOP")
lecturer2.setCoursesAttached("Git")
print(lecturer2.getCoursesAttached())
student1.EvaluationOfTheLecturerWork(lecturer2, "OOP", 9)
student1.EvaluationOfTheLecturerWork(lecturer2, "Git", 9)
# print(lecturer2.getGrades())
print(lecturer1.ComparisonOfLecturers(lecturer2))
print()

reviewer1 = Reviewer("Павел", "Молибог")
reviewer1.setCoursesAttached("OOP")

print(reviewer1)
print(reviewer1.getCoursesAttached())
print()

# reviewer1 оценил модуль "OOP"
reviewer1.AssessmentOfStudentWork(student1, "OOP", 10)
print(student1.getGrades())