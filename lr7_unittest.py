import unittest


class Test22(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Начнём же наши тесты!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Всем спасибо! Все свободны")

    def test_1(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        # В тесте test_1 проверяется сумма трёх чисел - должны быть равны 6

    def test_2(self):
        self.assertNotEqual(sum((1, 2, 2)), 6, "Should be 6")
        # В тесте test_2 проверяется сумма трёх чисел - не должны быть равны 6

    def test_3(self):
        self.assertAlmostEqual(22.0 / 7, 3.14, 2)
        # В тесте test_3 деление 22 / 7 находится в 2-х десятичных разрядах от 3, 14

    def test_4(self):
        self.assertGreater("B", "b", "Первый сравниваемый элемент точно не меньше")
        # В тесте test_4 сравнивается большая и маленькая буква. Тест не пройден, так как
        # в десятичной кодировке UTF-8 буква B - 66, а b - 98
        # Если поменять буквы местами, то тест пройдётся

    def test_5(self):
        self.assertCountEqual("abracadabra", "aaaaabbcdrr", "Не сходится количество символов")
        # В тесте test_5 сравнивается содержание тех же элементы в одинаковых количествах,
        # но порядок не важен. Тест пройден


if __name__ == '__main__':
    unittest.main()
