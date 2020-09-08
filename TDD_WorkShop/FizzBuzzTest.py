# FizzBuzzTest
# coding: UTF-8
import unittest


def convert(num):
    # 前準備
    # return 1
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


class TestConvert1(unittest.TestCase):
    """test class of FizzBuzz.py
    """

    def test_convert(self):
        # print('これは失敗するはず')
        """test method for「1を渡すと文字列"1"を返す」
        """
        # 実行 & 検証
        self.assertEqual("1", convert(1))

class TestConvert2(unittest.TestCase):
    """test class of FizzBuzz.py
    """

    def test_convert(self):
        """test method
        仕様：数をそのまま文字列に変換する
        具体：2を渡すと文字列"2"を返す
        """
        # 実行 & 検証
        self.assertEqual("2", convert(2))

class TestConvert3(unittest.TestCase):
    """test class of FizzBuzz.py
    """

    def test_convert(self):
        """test method
        仕様：3の倍数を
        具体：3を渡すと文字列"Fizz"を返す
        """
        # 実行 & 検証
        self.assertEqual("Fizz", convert(3))

class TestConvert5(unittest.TestCase):
    """test class of FizzBuzz.py
    """

    def test_convert(self):
        """test method
        具体：5を渡すと文字列"Buzz"を返す
        """
        # 実行 & 検証
        self.assertEqual("Buzz", convert(5))


if __name__ == '__main__':
    unittest.main()




"""
整数同士の割り算は、Pyrhon2までは整数が返っていたが、Python3からは浮動小数点を返すようになった。
"""