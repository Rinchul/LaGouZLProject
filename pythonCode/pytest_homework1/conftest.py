'''
1、补全计算器（加减乘除）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、conftest.py中创建fixture 完成setup和teardown
4、在调用测试方法之前打印【开始计算】，调用之后打印【计算结束】
'''
import pytest

from pythonCode.pytest_homework1.calculator import Calculator


@pytest.fixture(scope='class')
def cal():
    cal = Calculator()
    return cal
