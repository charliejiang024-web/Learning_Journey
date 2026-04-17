from person import Person

class Student(Person):  # 继承 Person
    def __init__(self, name, age, student_id):
        # 调用父类构造方法
        super().__init__(name, age)
        self.student_id = student_id
        self.scores = {}

    def add_score(self, subject, score):
        self.scores[subject] = score

    # 必须实现，否则报错
    def show_info(self):
        print(f"学生：{self.name}，学号：{self.student_id}")
        print("成绩：", self.scores)