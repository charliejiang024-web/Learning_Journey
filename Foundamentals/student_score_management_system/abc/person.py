from abc import ABC, abstractmethod

# 抽象基类：人
class Person(ABC):  # 继承 ABC，变成抽象类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 抽象方法：子类必须实现！不写就报错
    @abstractmethod
    def show_info(self):
        pass

