# Integer closed interval
# coding: UTF-8
import unittest



def is_integer_num(num):
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return num.is_integer()
    return False



class ClosedInterval:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def make_integer_closed_interval(self):
        """
        整数閉区間を生成して返す関数
        """
        # return self.num1, self.num2
        str1 = str(self.num1)
        str2 = str(self.num2)

        if is_integer_num(self.num1) and is_integer_num(self.num2):
            if self.num1 < self.num2:
                return "[" + str1 + ", " + str2 + "]"
            else:
                return "閉区間を作れません"
        else:
            return "閉区間を作れません"


    def judge_integer_included(self, num3):
        """
        閉じた区間が指定した整数を含むかどうかを判定する
        """
        if self.num1 <= num3 and self.num2 >= num3:
            return "整数が閉区間に含まれる"
        else:
            return "整数が閉区間に含まれない"


    def judge_other_interval_included(self, interval):
        """
        閉じた区間が指定した整数を含むかどうかを判定する
        """
        other_num1 = interval[0]
        other_num2 = interval[1]

        if other_num1 >= self.num1 and other_num2 <= self.num2:
            return "他の閉区間を含む"
        else: 
            return "他の閉区間を含まない"
    


class TestArgumentIsIntegrate(unittest.TestCase):
    """IntegerClosedInterval.py をテストするクラス
    """
    def test_argument_is_integrate(self):
        # print('これは失敗するはず')
        """1と2を引数にとれる
        """
        # 前準備
        CI = ClosedInterval(1, 2)
        # 実行
        result = CI.make_integer_closed_interval
        # 検証
        # print(CI.make_integer_closed_interval())
        # self.assertEqual((1, 2), CI.make_integer_closed_interval())


class TestReturnStringClosedInterval(unittest.TestCase):
    def test_return_string_closed_interval(self):
        """(1, 2)を入力すると("[1, 2]")を返却する
        """
        # 前準備
        CI = ClosedInterval(1, 2)
        # 実行 & 検証
        # print(CI.make_integer_closed_interval)
        self.assertEqual("[1, 2]", CI.make_integer_closed_interval())

class TestCheckIntegrate(unittest.TestCase):
    def test_check_integrate(self):
        """(0.1, 2)を入力すると"閉区間を作れません"と返す
        """
        # 前準備
        CI = ClosedInterval(0.1, 2)
        # 実行 & 検証
        # print(CI.make_integer_closed_interval)
        self.assertEqual("閉区間を作れません", CI.make_integer_closed_interval())
        
class TestCheckUpperLower(unittest.TestCase):
    def test_check_upper_lower(self):
        """上端点=1, 下端点=2 を入力すると"閉区間を作れません"と返す
        """
        CI = ClosedInterval(2, 1)
        self.assertEqual("閉区間を作れません", CI.make_integer_closed_interval())


class TestJudgeIntegerIncluded(unittest.TestCase):
    def test_check_integer_included(self):
        """閉区間[1, 3]が2を含む場合"整数が閉区間に含まれる"と返す
        """
        CI = ClosedInterval(1, 3)
        self.assertEqual("整数が閉区間に含まれる", CI.judge_integer_included(2))

class TestJudgeIntegerIncluded(unittest.TestCase):
    def test_check_integer_included(self):
        """閉区間[1, 3]が4を含まない場合"整数が閉区間に含まれない"と返す
        """
        CI = ClosedInterval(1, 3)
        self.assertEqual("整数が閉区間に含まれない", CI.judge_integer_included(4))


class TestJudgeOtherIntervalIncluded(unittest.TestCase):
    def test_other_interval_included(self):
        """閉区間[1, 4]が他の閉区間[2, 3]を含む場合"他の閉区間を含む"と返す
        """
        CI = ClosedInterval(1, 4)
        self.assertEqual("他の閉区間を含む", CI.judge_other_interval_included([2, 3]))

class TestJudgeOtherIntervalIncluded(unittest.TestCase):
    def test_other_interval_included(self):
        """閉区間[1, 4]が他の閉区間[2, 5]を含まない場合"他の閉区間を含まない"と返す
        """
        CI = ClosedInterval(1, 4)
        self.assertEqual("他の閉区間を含まない", CI.judge_other_interval_included([2, 5]))



if __name__ == '__main__':
    unittest.main()


"""
python -m unittest -v IntegerClosedInterval
"""

"""フィードバック
printではなくassertを使う（printは人の目で見て確認する必要があるので自動でデバックできない）
OKかFAILに落とし込む
"""


"""問題文 https://bit.ly/2uEATGA
整数閉区間を示すクラス（あるいは構造体）をつくりたい。整数閉区間オブジェクトは下端点と上端点を持ち、文字列表現も返せる（例: 下端点 3, 上端点 8 の整数閉区間の文字列表記は "[3,8]"）。
ただし、上端点より下端点が大きい閉区間を作ることはできない。整数の閉区間は指定した整数を含むかどうかを判定できる。また、別の閉区間と等価かどうかや、完全に含まれるかどうかも判定できる。
"""
"""to do リスト
【整数閉区間を示すクラスをつくる】

-[○] 下端点と上端点の２つの値を 引数1 引数2 とする                                   -> ★整数閉区間★

  -[○]２つの引数から "[引数1, 引数2]" という文字列表現を返す                           -> ★下端点と上端点の文字列表現を返す★

  -[○] 引数1 と 引数2 が整数でない場合は "閉区間を作れません" を返す

  -[○] 引数2 < 引数1 の場合は "閉区間を作れません" を返す                             -> ★上端点より下端点が大きい閉区間を作ることはできない★


-[] 整数を 引数3 とする                                                          -> 指定した整数を含むかどうかを判定する
  -[] 引数3 がない場合は 何もしない
    -[] 引数3 > 引数1 かつ 引数3 < 引数2 の場合 "整数が閉区間に含まれる" と返す


-[] 別の閉区間を 引数4 とする
  -[] 引数4 がない場合は 何もしない
  -[] 引数4 がある場合は 引数4 から下端点(引数4.1)と上端点(引数4.2)を引き出す
    - [] 引数4.1 = 引数1 かつ 引数4.2 = 2 の場合は "別のの閉区間と等価である" と返す   -> ★別の閉区間と等価かどうかを判定する★
    - [] 引数4.1 < 引数1　引数4.2 > 引数2 の場合は "別の閉区間が完全に含まれる" と返す  -> ★別の閉区間が完全に含まれるかどうかを判定する★
"""