# -*- coding: utf-8 -*-


from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from 臺灣言語工具.系統整合.外部程式 import 外部程式
from 臺灣言語工具.語言模型.安裝KenLM訓練程式 import 安裝KenLM訓練程式
from os import makedirs
from os.path import join, isfile


class KenLM語言模型訓練(程式腳本):

    def __init__(self,
                 kenlm安裝路徑=外部程式.目錄(),
                 moses資料夾路徑=外部程式.moses預設目錄()
                 ):
        kenlm訓練指令 = join(安裝KenLM訓練程式.kenlm資料夾路徑(kenlm安裝路徑), 'bin', 'lmplz')
        moses訓練指令 = join(moses資料夾路徑, 'bin', 'lmplz')
        self.訓練指令 = None
        if isfile(kenlm訓練指令):
            self.訓練指令 = kenlm訓練指令
        elif isfile(moses訓練指令):
            self.訓練指令 = moses訓練指令
        if self.訓練指令 is None:
            raise FileNotFoundError('佇{0}揣無KenLM執行檔！！'.format(self.訓練指令))
        print(self.訓練指令)
        self.訓練指令 = join(moses資料夾路徑, 'bin', 'lmplz')

    def 訓練(self, 語料陣列,
           暫存資料夾,
           連紲詞長度=3,
           編碼器=無編碼器(),
           使用記憶體量='20%',
           ):
        makedirs(暫存資料夾, exist_ok=True)
        目標語言全部語料檔名 = join(暫存資料夾, '語言模型.txt')
        self._檔案合做一个(目標語言全部語料檔名, 語料陣列, 編碼器)
        語言模型檔 = join(暫存資料夾, '語言模型.lm')
# 		語言模型指令版 = \
# 			'{0} -o {1} -S {4} -T /tmp < {2} > {3}'
# 		語言模型指令 = 語言模型指令版.format(
# 			self.訓練指令,
# 			連紲詞長度,
# 			目標語言語料檔名,
# 			語言模型檔,
# 			使用記憶體量,
# 			)
        with open(目標語言全部語料檔名, 'r') as 目標語言全部語料:
            with open(語言模型檔, 'w') as 語言模型:
                self._走指令(
                    [
                        self.訓練指令,
                        '-o', str(連紲詞長度),
                        '--discount_fallback',
                        '-S', 使用記憶體量,
                        '-T', '/tmp',
                    ],
                    stdin=目標語言全部語料,
                    stdout=語言模型,
                )
        return 語言模型檔
