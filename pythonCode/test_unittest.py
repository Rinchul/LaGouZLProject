import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual('a', 'a', '不相等')

    def test_case02(self):
        print("test_case02")
        self.assertIn(1, [1, 2, 3], '不包含')

    @unittest.skipIf(True, "跳过此用例")
    def test_case03(self):
        print("test_case03")
        self.assertTrue(True, "不为真")


class demo1(unittest.TestCase):
    def test_demo1_case01(self):
        print("test_demo1_case01")

    def test_demo1_case02(self):
        print("test_demo1_case02")


class demo2(unittest.TestCase):
    def test_demo2_case01(self):
        print("test_demo2_case01")

    def test_demo2_case02(self):
        print("test_demo2_case02")


if __name__ == '__main__':
    # 执行方法一：执行当前模块所有用例
    # unittest.main()

    # 执行方法二：加入容器中执行
    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_demo1_case01"))
    # unittest.TextTestRunner().run(suite)

    # 执行方法三：同时执行多个测试类
    # suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # all = unittest.TestSuite([suite, suite1])
    # unittest.TextTestRunner().run(all)

    # 执行方法四：匹配目录下所有以test开头的py文件，执行文件下所有用例
    discover = unittest.defaultTestLoader.discover("./", 'test*.py')
    unittest.TextTestRunner.run(discover)
