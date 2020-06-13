"""
创建Bicycle（自行车）类
    方法：run(),参数：int里程
创建EBicycle继承Bicycle
    属性：battery_level电池电量
    方法：fill_charge(vol)充电，vol为电量
        run(km)骑行
需求：每10km消耗1度电
    当电量耗尽时调用Bicycle的run()骑行
    通过传入的骑行里程数显示骑行结果
"""
import yaml


class Bicycle:
    def run(self, km):
        print(f"骑行的里程数为：{km}km")


class EBicycle(Bicycle):
    def __init__(self, battery_level):
        self.battery_level = battery_level

    def fill_charge(self, vol):
        print(f"充电：{vol}")

    def run(self, km):
        max_mile = self.battery_level * 10
        leave_mile = km - max_mile

        if leave_mile > 0:
            print(f"已经使用电量骑行的里程数：{max_mile}km")
            # 调用父类run()
            super().run(leave_mile)
        else:
            print(f"骑行的里程数：{km}")


if __name__ == "__main__":
    with open("data.yml") as f:
        datas = yaml.safe_load(f)
    print(datas)
    my1 = datas['default']
    my1_battery = my1['battery_level']
    my1_km = my1['km']
    print(my1)
    print(my1_battery)
    print(my1_km)

# my_ebicycle = EBicycle(10)
# my_ebicycle.run(107)
