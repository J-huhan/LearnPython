class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score =score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('lisa',90)
bar = Student('bar',60)
print(lisa.get_grade())
print(bar._Student__name,bar.get_grade())

