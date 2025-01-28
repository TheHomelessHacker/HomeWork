class Student():

    def __init__(self, nameStudent, surnameStudent, genderStudent):
        self.__name = nameStudent
        self.__surname = surnameStudent
        self.__gender = genderStudent
        # инициализируем этот атрибут для каждого экземпляра по отдельности
        # и у каждого студента будут свои пройденные курсы.
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

    # ! попробовать через map написать, как правильно вывести инф по человеку
    # через print или через retutn?
    def getAvarageGrade(self):
        overallAssessments = 0
        countOfAssesments = 0
        for grade in self.__grades.values():
            overallAssessments += sum(grade)
            countOfAssesments += len(grade)
        # print(f"Средний балл по всем курсам у студента {self.getNameStudent()}"
        #       f"составляет {overallAssessments / countOfAssesments}")
        return overallAssessments / countOfAssesments
    
    # Не знаю пока как правильно обработать случай, что у студента нет оценок 
    # по курсу, это надо через print? или через Error, или ещё как-нибудь
    # как правильно вывести инф по человеку через print или через retutn?
    def getAvarageGradeOneCourse(self, nameCourse):
        overallAssessments = 0
        countOfAssesments = 0
        if nameCourse in self.__grades:
            overallAssessments= sum(self.__grades[nameCourse])
            countOfAssesments = len(self.__grades[nameCourse])
            # print(f"Средний балл по курсу {nameCourse} у студента"
            #     f"{self.getNameStudent()} составляет {overallAssessments / countOfAssesments}")
            return overallAssessments / countOfAssesments
        else:
            #KeyError "У студента нет оценок по курсу!!"
            # print("У студента нет оценок по курсу!!")
            return 0
    
    def getFinishCourses(self):
        finishCourses = ''
        for course in self.__finishedCourses:
            finishCourses += course + ', '
        finishCourses = finishCourses.rstrip(", ")
        if finishCourses == '':
            return "Их нет"
        else:
            return finishCourses

    def getInProgressCourses(self):
        inProgressCourses = ''
        for course in self.__coursesInProgress:
            inProgressCourses += course + ', '
        inProgressCourses = inProgressCourses.rstrip(", ")
        return inProgressCourses

    '''-------------------------------------------------'''

    def setNameStudent(self, name):
        self.__name = name

    def setSurnameStudent(self, surname):
        self.__surname = surname

    def setGender(self, gender):
        self.__gender = gender

    def setFinishedCourses(self, finishedCourses):
        self.__finishedCourses.extend(finishedCourses)

    # Попытался сделать так, что если курса в нет в списке тех, которые в 
    # процессе узучения, то добавить, но там все сломалось, поправить позже !!!
    def setGrades(self, grades):
        self.__grades.update(grades)
        # if grades.keys() not in self.getCoursesInProgress():
        #     self.setCoursesInProgress(grades.keys())

    def setCoursesInProgress(self, coursesInProgress):
        self.__coursesInProgress.append(coursesInProgress)

    # ? не очень понимаю как правильно обработать grade > 10
    def EvaluationOfTheLecturerWork(self, lecturer, course, grade):
        if  0 <= grade <= 10:
            if isinstance(lecturer, Lecturer) and course in lecturer.getCoursesAttached() and course in self.getCoursesInProgress():
                if course in lecturer.getGrades():
                    lecturer.getGrades()[course] += [grade]
                else:
                    lecturer.getGrades()[course] = [grade]
                return f"Студент {self.getNameStudent()} оценил лектора {lecturer.getName()} на отметку {grade}"
                # print(f"Студент {self.getNameStudent()} оценил лектора {lecturer.getName()} на отметку {grade}")
            else:
                return f"Лектор {lecturer.getName} не прикреплён к курсу {course}"
                # print(f"Лектор {lecturer.getName} не прикреплён к курсу {course}")
        else:
            print("У нас 10-ти бальная система оценивания!")
        
    # ! переделать с использованием фолшебный методов
    def ComparisonOfStudents(self, student2):
        if self.getAvarageGrade() > student2.getAvarageGrade():
            return (f"В сравнении студентов {self.getNameStudent()} и {student2.getNameStudent()}\n"
                    f"Лучше оказался студент {self.getNameStudent()} со средним баллом {self.getAvarageGrade()}")
        elif self.getAvarageGrade() < student2.getAvarageGrade():
            return (f"В сравнении студентов {self.getNameStudent()} и {student2.getNameStudent()}\n"
                    f"Лучше оказался студент {student2.getNameStudent()} со средним баллом {self.getAvarageGrade()}")
        else:
            return f"студенты {self.getNameStudent()} и {student2.getNameStudent()} имеют одинаковый средний балл {self.getAvarageGrade()}"

    def __eq__(self, other):
        if self.getAvarageGrade() == other.getAvarageGrade():
            print(f"Студенты {self.getNameStudent()} и {other.getNameStudent()} имеют одинаковый средний балл {self.getAvarageGrade()}")
        else:
            print(f"Студенты {self.getNameStudent()} и {other.getNameStudent()} имеют разный средний балл {self.getAvarageGrade()} и {other.getAvarageGrade()}")
        return self.getAvarageGrade() == other.getAvarageGrade()

    def __gt__(self, other):
        if self.getAvarageGrade() > other.getAvarageGrade():
            print(f"Лучше оказался студент {self.getNameStudent()} со средним баллом {self.getAvarageGrade()}")
        else:
            print(f"Лучше оказался студент {other.getNameStudent()} со средним баллом {other.getAvarageGrade()}")
        return self.getAvarageGrade() > other.getAvarageGrade()

    def __str__(self):
        # вот правильно
        return (f"Имя: {self.__name}\n"
                f"Фамилия: {self.__surname}\n"
                f"Средняя оценка за домашние задания: {self.getAvarageGrade()}\n"
                f"Курсы в процессе изучения: {self.getInProgressCourses()}\n"
                f"Завершенные курсы: {self.getFinishCourses()}\n")
        # вот так неправильно 
#         return f"Имя: {self.__name}\n\
# Фамилия: {self.__surname}\n\
# Средняя оценка за домашние задания: {self.getAvarageGrade()}\n\
# Курсы в процессе изучения: {self.getInProgressCourses()}\n\
# Завершенные курсы: {self.getFinishCourses()}"


class Mentor:

    def __init__(self, nameMentor, surnameMentor):
        self.__name = nameMentor
        self.__surname = surnameMentor
        self.__coursesAttached = []
    
    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname
    
    def getCoursesAttached(self):
        return self.__coursesAttached

    def setName(self, name):
        self.__name = name
    
    def setSurname(self, surname):
        self.__surname = surname

    def setCoursesAttached(self, coursesAttached):
        self.__coursesAttached.append(coursesAttached)
    
    def __str__(self):
        return f"Преподаватель {self.__name} {self.__surname}"

    
class Lecturer(Mentor):

    def __init__(self, nameMentor, surnameMentor):
        super().__init__(nameMentor, surnameMentor)
        self.__coursesAttached = []
        self.__grades = {}

    def getCoursesAttached(self):
        if self.__coursesAttached == []:
            return f"Лектор {self.getName()} не закреплён ни за одним курсом"
        else:
            return f"Вот курсы - {self.__coursesAttached} за которыми закреплён преподаватель {self.getName()}" 
        # return self.__courses_attached

    def getGrades(self):
        return self.__grades

    def setCoursesAttached(self, coursesAttached):
        self.__coursesAttached.append(coursesAttached)

    def setGrades(self, grades):
        self.__grades.update(grades)

    def getAvarageGrade(self):
        overallAssessments = 0
        countOfAssesments = 0
        for grade in self.__grades.values():
            overallAssessments += sum(grade)
            countOfAssesments += len(grade)
        return overallAssessments / countOfAssesments

    def getAvarageGradeOneCourse(self, nameCourse):
        overallAssessments = 0
        countOfAssesments = 0
        if nameCourse in self.__grades:
            overallAssessments= sum(self.__grades[nameCourse])
            countOfAssesments = len(self.__grades[nameCourse])
            return overallAssessments / countOfAssesments
        else:
            #KeyError "У лектора нет оценок по курсу!!"
            return 0

    # ! переделять при помощи магических методов
    def comparisonOfLecturers(self, lecturer2):
        if self.getAvarageGrade() > lecturer2.getAvarageGrade():
            return f"Лучше оказался преподавтель {self.getName()}"
        elif self.getAvarageGrade() < lecturer2.getAvarageGrade():
            return f"Лучше оказался преподавтель {lecturer2.getName()}"
        else:
            return f"Преподаватели {self.getName()} и {lecturer2.getName()} получили от студентов одинаковые оценки"

    def __eq__(self, other):
        if self.getAvarageGrade() == other.getAvarageGrade():
            print(f"Преподаватели {self.getName()} и {other.getName()} получили от студентов одинаковые оценки")
        else:
            print(f"Преподаватели {self.getName()} и {other.getName()} получили от студентов разные оценки")
        return self.getAvarageGrade() == other.getAvarageGrade()

    def __gt__(self, other):
        if self.getAvarageGrade() > other.getAvarageGrade():
            print(f"Лучше оказался преподавтель {self.getName()}")
        else:
            print(f"Лучше оказался преподавтель {other.getName()}")
        return self.getAvarageGrade() > other.getAvarageGrade()


    def __str__(self):
        return (f"Имя: {self.getName()}\n"
                f"Фамилия: {self.getSurname()}\n"
                f"Средняя оценка за лекции: {self.getAvarageGrade()}\n")


class Reviewer(Mentor):
    def __init__(self, nameMentor, surnameMentor):
        super().__init__(nameMentor, surnameMentor)
        self.__coursesAttached = []

    def getCoursesAttached(self):
        return f"Reviewer {self.getName()} закреплен за курсами:{self.__coursesAttached}"

    def setCoursesAttached(self, coursesAttached):
        self.__coursesAttached.append(coursesAttached)

    def AssessmentOfStudentWork(self, student, course, grade):
        if isinstance(student, Student) and course in self.__coursesAttached and course in student.getCoursesInProgress():
            if course in student.getGrades():
                student.getGrades()[course] += [grade]
            else:
                student.getGrades()[course] = [grade]
            print(f"Преподаватель {self.getName()} поставил оценку {grade} студенту {student.getNameStudent()} по теме {course}")
        else:
            return 'Ошибка'
    
    def __str__(self):
        return (f"Имя: {self.getName()}\n"
                f"Фамилия: {self.getSurname()}\n")
    

# Обработать доп случаю когда у кого-то курс завершился, у кого то нет
def avarageGrageStudent(listName, nameCourse):
    countOfStudent = 0
    avarageGrage_ = 0
    for name in listName:
        if nameCourse in name.getInProgressCourses():
            countOfStudent += 1
            avarageGrage_ += name.getAvarageGradeOneCourse(nameCourse)
        elif nameCourse in name.getFinishCourses():
            countOfStudent += 1
            avarageGrage_ += name.getAvarageGradeOneCourse(nameCourse)
        
    return (f"В списке было {len(listName)} студентов, и из них по курсу есть оценки у {countOfStudent} студентов,"
            f"а их общий средний балл по курсу {nameCourse} составил: {avarageGrage_ / countOfStudent}")

def avarageGrageLecturer(listName, nameCourse):
    countOfLecturer = 0
    avarageGrage_ = 0
    for name in listName:
        if nameCourse in name.getCoursesAttached():
            countOfLecturer += 1
            avarageGrage_ += name.getAvarageGradeOneCourse(nameCourse)
        else:
            print("Error")
        
    return (f"В списке было {len(listName)} лекторов, и из них по курсу есть оценки у {countOfLecturer} лекторов,"
            f"а их общий средний балл по курсу {nameCourse} составил: {avarageGrage_ / countOfLecturer}")

listStudent = []
listLecturer = []

student1 = Student('Mark', 'Zdorovets', 'man')
listStudent.append(student1)
# ? как праильно реализовать добавление може быть 1 или срузу несколько(зависит от задачаи)
student1.setCoursesInProgress("OOP")
# ? как праильно реализовать добавление може быть 1 или срузу несколько(зависит от задачаи)
student1.setFinishedCourses(['Python', 'Git'])
student1.setGrades({'Python': [10, 10, 10]})
student1.setGrades({'Git': [10, 10, 10]})
print(student1)

student2 = Student("Elon", "Mask", "robot")
listStudent.append(student2)
student2.setCoursesInProgress("Python")
student2.setGrades({'Python': [9, 9, 7]})
print(student2)
print(f'Средний балл у стедента Elon Mask по курсу Python: {student2.getAvarageGradeOneCourse("Python")}\n')

student3 = Student("Jef", "Bezos", "robot")
listStudent.append(student3)
student1.setCoursesInProgress("Python")
student3.setGrades({'Python': [8, 8, 7]})
# print(student3)

student1.__eq__(student2)
student1.__gt__(student2)
# print(student1.ComparisonOfStudents(student2), '\n')

lecturer1 = Lecturer("Peta", "W")
listLecturer.append(lecturer1)
print(lecturer1.getCoursesAttached())
lecturer1.setCoursesAttached("OOP")
print(lecturer1.getCoursesAttached())
student1.EvaluationOfTheLecturerWork(lecturer1, "OOP", 10)
print(lecturer1.getGrades())
print(lecturer1)

lecturer2 = Lecturer("Anna", "K")
listLecturer.append(lecturer2)
lecturer2.setCoursesAttached("OOP")
print(lecturer2.getCoursesAttached())
lecturer2.setCoursesAttached("Git")
print(lecturer2.getCoursesAttached())
student1.EvaluationOfTheLecturerWork(lecturer2, "OOP", 9)
student1.EvaluationOfTheLecturerWork(lecturer2, "Git", 9)
print()
lecturer1.__eq__(lecturer2)
lecturer1.__gt__(lecturer2)
print()

reviewer1 = Reviewer("Павел", "Молибог")
reviewer1.setCoursesAttached("OOP")

print(reviewer1)
print(reviewer1.getCoursesAttached(), '\n')

# reviewer1 оценил модуль "OOP"
print(f"Оценки студента Mark {student1.getGrades()}\n")
reviewer1.AssessmentOfStudentWork(student1, "OOP", 10)
print(f"Оценки студента Mark {student1.getGrades()}\n")

print(avarageGrageStudent(listStudent, "OOP"))
print(avarageGrageLecturer(listLecturer, "OOP"))