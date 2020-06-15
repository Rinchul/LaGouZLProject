import allure
import pytest
import yaml


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


# 参数化
@pytest.mark.parametrize(['a', 'b'], yaml.safe_load(open("./data_pytest.yml")))
def test_answer(a, b):
    assert inc(a) == b


# 方法的返回作为参数传递
@pytest.fixture(scope='class', params=[1, 2, 3, 'Job'])
def login():
    username = 'Tom'
    return username


@allure.feature('功能名称')
class TestDemo:
    @allure.story('test_a')
    def test_a(self, login):
        with allure.step('步骤一'):
            print('步骤一')
        with allure.step('步骤二'):
            print('步骤二')
        print(f'a login={login}')

    @allure.step('方法步骤')
    def test_b(self):
        print('b')

    @pytest.mark.usefixtures('login')
    def test_abc(self):
        print(f'abc login={login}')


if __name__ == '__main__':
    pytest.main(['test_pytest.py::TestDemo', '-v'])
