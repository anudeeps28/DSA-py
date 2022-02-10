# Object Oriented Programming in Python
# Creating a more complex object

# advantege of using multiple classes instead of using one class


class Student:
    def __init__(self,name,age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course: #defining another class
    def __init__(self, name, max_students): #every attribute has to be declared while making an object of the class 
        self.name = name
        self.max_students = max_students
        self.students = [] 

    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        #pass #if we do not write this pass, all that is below this def will be counted as inside 
            # def and error will show to indent the block

        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)
s1 = Student("Tim", 19,95) #making students: objects of class Student
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2) #making course: object course of class Course

course.add_student(s1)
course.add_student(s2)

# prints: [<__main__.Student object at 0x1029fadf0>, <__main__.Student object at 0x1029fad90>]
# means that both our sourses are student objects
print(course.students)

# this prints the name
print(course.students[0].name)
print(course.students[1].age)
print(course.get_average_grade()) #this will print the average of all the grades of s1,s2 and s3

# the idea = we can have different classes with different attributes and we can program them in a different style to interact with them
# thus, we can make classes interact with each other

