# -*- coding: utf-8 -*-
import os
from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本

class 斯里語句連詞訓練(程式腳本):
	'SRILM'
	def 訓練(self, 語料,
			暫存資料夾,
			連紲詞長度=3,
			編碼器=無編碼器(),
			SRILM執行檔路徑=''):
		os.makedirs(暫存資料夾, exist_ok=True)
		目標語言檔名 = os.path.join(暫存資料夾, '語言模型.txt')
		self._檔案合做一个(目標語言檔名, 語料, 編碼器)
		語言模型檔 = os.path.join(暫存資料夾, '語言模型.lm')
		語言模型指令版 = \
			'{0}ngram-count -order {1} -interpolate -wbdiscount -unk -text {2} -lm {3}'
		語言模型指令 = 語言模型指令版.format(
			self._執行檔路徑加尾(SRILM執行檔路徑),
			連紲詞長度,
			目標語言檔名,
			語言模型檔
			)
		self._走指令(語言模型指令)
		return 語言模型檔
