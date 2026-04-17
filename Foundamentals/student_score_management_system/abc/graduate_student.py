from student import Student

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, supervisor, thesis):
        super().__init__(name, age, student_id)
        self.supervisor = supervisor  # 导师
        self.thesis = thesis          # 论文

    # 重写（覆盖）父类方法
    def show_info(self):
        print(f"研究生：{self.name}，导师：{self.supervisor}")
        print(f"论文：{self.thesis}")
        print("成绩：", self.scores)