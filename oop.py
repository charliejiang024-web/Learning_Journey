from dataclasses import dataclass

class Person: # 一类东西，比如说大雁，动物，人等
    count = 0 # count 叫做类属性，所有Person实例共享
    def __init__(self, name, age):# 这个叫做“构造方法”
        self.name = name # 这个self.name指的是你定义的实例属性，每个实例都有自己的name属性
        self.age = age 
        Person.count += 1

    #我们可以在下面定义一个“实例方法”
    def introduce(self):
        return f"我是{self.name}, 我今年{self.age}岁"
    
    @staticmethod # 这个方法不关类和实例一点屁事，只是一个普通的函数
    def is_adult(age):
        return age >= 18

person_1 = Person('james', 18) # 这个是独立的实例对象
print(person_1.introduce()) 
print(person_1.count) # 类属性不是方法，不用加（）
# 这种是不推荐的，最好是直接：
print(Person.count)


# 数据类，用这个的好处是自动生成init等方法
@dataclass
class Person1():
    name:str = ""
    age:int = 0

person_2 = Person1('date', 20)
print(person_2)