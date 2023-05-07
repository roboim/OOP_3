class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        grade = 0.0
        grade = self.ave_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {grade}\n" \
               f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершённые курсы: {', '.join(self.finished_courses)}\n"

    def __lt__(self, second_student):
        if isinstance(second_student, Student):
            if second_student.ave_grade() > self.ave_grade():
                return True
            else:
                return False
        else:
            return 'Ошибка'
    def ave_grade(self):
        results = []
        results = [sum(self.grades[grade])/len(self.grades[grade]) for grade in self.grades]
        grade = 0.0
        grade = sum(results)/len(results)
        return grade

    def set_grade_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                course in self.courses_in_progress:
            if 0 < int(grade) < 11:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка выставления оценки'
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        grade = 0.0
        grade = self.ave_grade()
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {grade}\n"

    def __lt__(self, second_lecturer):
        if isinstance(second_lecturer, Lecturer):
            if second_lecturer.ave_grade() > self.ave_grade():
                return True
            else:
                return False
        else:
            return 'Ошибка'
    def ave_grade(self):
        results = []
        results = [sum(self.grades[grade])/len(self.grades[grade]) for grade in self.grades]
        grade = 0.0
        grade = sum(results)/len(results)
        return grade

class Reviewer(Mentor):
    def set_grade_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

good_student = Student('Иван', 'Петров', 'your_gender')
good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Git']
good_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Сергей', 'Петров')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

good_lecturer = Lecturer('Иван', 'Иванов')
good_lecturer.courses_attached += ['Python']
good_lecturer.courses_attached += ['Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.set_grade_student(best_student, 'Python', 10)
cool_reviewer.set_grade_student(best_student, 'Python', 10)
cool_reviewer.set_grade_student(best_student, 'Git', 9)
cool_reviewer.set_grade_student(best_student, 'Git', 9)

cool_reviewer.set_grade_student(good_student, 'Python', 9)
cool_reviewer.set_grade_student(good_student, 'Python', 9)
cool_reviewer.set_grade_student(good_student, 'Git', 9)
cool_reviewer.set_grade_student(good_student, 'Git', 9)

best_student.set_grade_lecturer(cool_lecturer, 'Python', 10)
best_student.set_grade_lecturer(cool_lecturer, 'Python', 10)
best_student.set_grade_lecturer(cool_lecturer, 'Git', 10)
best_student.set_grade_lecturer(cool_lecturer, 'Git', 10)

best_student.set_grade_lecturer(good_lecturer, 'Python', 9)
best_student.set_grade_lecturer(good_lecturer, 'Python', 9)
best_student.set_grade_lecturer(good_lecturer, 'Git', 10)
best_student.set_grade_lecturer(good_lecturer, 'Git', 10)

# print(cool_lecturer)
# print(good_lecturer)
# print(good_lecturer)
# print(best_student)
# print(good_student)

print(cool_reviewer)
print(cool_lecturer)
print(best_student)
print(cool_lecturer > good_lecturer)
print(best_student > good_student)
