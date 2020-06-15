import pytest
import yaml

f = yaml.safe_load(open("./cal_data.yml", encoding='UTF-8'))
print(f)


@pytest.fixture()
def log():
    print('开始计算')
    yield None
    print('计算结束')


class TestCalculator:
    @pytest.mark.parametrize(['a', 'b', 'value'], f['add'])
    def test_add(self, cal, a, b, value, log):
        assert value == cal.add(a, b)

    @pytest.mark.parametrize(['a', 'b', 'value'], f['sub'])
    def test_sub(self, cal, a, b, value, log):
        assert value == cal.sub(a, b)

    @pytest.mark.parametrize(['a', 'b', 'value'], f['mul'])
    def test_mul(self, cal, a, b, value, log):
        assert value == cal.mul(a, b)

    @pytest.mark.parametrize(['a', 'b', 'value'], f['div'])
    def test_div(self, cal, a, b, value, log):
        assert value == cal.div(a, b)
