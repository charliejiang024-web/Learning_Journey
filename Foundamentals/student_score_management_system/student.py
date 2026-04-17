class Student:
    # 考虑构造函数在设计上的作用
    # 学生必须包含名字和学号
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.scores ={}

    # 科目和成绩
    def add_score(self,subject,score):
        self.scores[subject] = score

# 方法：计算平均分
    def get_average(self):
        if not self.scores:  # 如果没有成绩
            return 0
        return sum(self.scores.values()) / len(self.scores)

    # 方法：显示学生所有信息
    def show_info(self):
        print(f"===== 学生：{self.name} (学号：{self.student_id}) =====")
        print("成绩：")
        for sub, score in self.scores.items():
            print(f"  {sub}：{score} 分")
        print(f"平均分：{self.get_average():.1f}\n")

