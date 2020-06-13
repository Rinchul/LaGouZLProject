"""
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=短毛，
- 添加一个新的方法， 会捉老鼠，
- 复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】
创建一个猫猫实例
- 调用捉老鼠的方法
- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
"""
import yaml


class Animal:
    def __init__(self, name, colour, age, gender):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender

    def call(self):
        print(f'{self.name} can call')

    def run(self):
        print(f'{self.name} can run')


class Cat(Animal):
    def __init__(self, name, colour, age, gender, hair='短毛'):
        super().__init__(name, colour, age, gender)
        self.hair = hair

    def catch_mouse(self):
        print(f'{self.name} can catch mouse')

    def call(self):
        print(f'{self.name} can "喵喵叫"')


class Dog(Animal):
    def __init__(self, name, colour, age, gender, hair='长毛'):
        super().__init__(name, colour, age, gender)
        self.hair = hair

    def look_after_home(self):
        print(f'{self.name} can look after home')

    def call(self):
        print(f'{self.name} can "汪汪叫"')


if __name__ == "__main__":
    with open("animal_data.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    print(datas)
    animal1 = datas['animal1']
    animal2 = datas['animal2']

cat = Cat(animal1["name"], animal1["colour"], animal1["age"], animal1["gender"])
cat.call()
print(f'猫猫的姓名：{cat.name},颜色：{cat.colour},年龄：{cat.age}岁,性别：{cat.gender},毛发：{cat.hair}')
cat.catch_mouse()

dog = Dog(animal2["name"], animal2["colour"], animal2["age"], animal2["gender"])
print(f'狗狗的姓名：{dog.name},颜色：{dog.colour},年龄：{dog.age}岁,性别：{dog.gender},毛发：{dog.hair}')
dog.call()
dog.look_after_home()
