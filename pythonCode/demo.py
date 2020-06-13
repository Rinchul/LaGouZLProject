"""
创建一个Person类
    属性：姓名，性别，年龄，存款金额
    方法：吃，睡，跑，赚钱
创建FunnyMan类（喜剧演员）
    继承父类Person的所有属性和方法
    新增一个方法，fun()搞笑
创建SingerMan类（歌手演员）
    继承父类Person的所有属性和方法
    覆写方法赚钱，传参(money)
"""


class Person:
    def __init__(self, name: str, gender: str, age: int, money: float):
        self.name = name
        self.gender = gender
        self.age = age
        self.__money = money

    def get_money(self):
        return self.__money

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name} is running")

    def make_money(self):
        print(f"{self.name} can make money")


class FunnyMan(Person):
    def fun(self):
        print(f"{self.name} is funny")


class SingerMan(Person):
    def make_money(self, money: str):
        print(f"{self.name} can make money {money}")


class Programer(Person):
    def coding(self):
        print(f"{self.name} is coding")

    # 类方法
    @classmethod
    def write(cls):
        print("Anyone can write")

    # 静态方法
    @staticmethod
    def static():
        print("这是一个静态方法")


man = Programer("Job", "男", 28, 8000)
man.write()
Programer.write()
Programer.static()

singer = SingerMan("Jerry", "男", 23, 10000)
singer.make_money("5000")

funnyman = FunnyMan("Tom", "男", 20, 1000)
funnyman.run()
funnyman.fun()

p = Person("Sally", "女", 18, 2000)
print(p.get_money())
p.eat()
dir(p)  # 获取p可调用的所有方法和属性
