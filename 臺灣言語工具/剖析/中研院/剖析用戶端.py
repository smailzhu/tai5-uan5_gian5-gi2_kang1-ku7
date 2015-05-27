# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import sys
import time


from 臺灣言語工具.斷詞.中研院.用戶端連線 import 用戶端連線

class 剖析用戶端(用戶端連線):
	def __init__(self, 主機='140.109.19.112', 連接埠=8000, 編碼='Big5',
			帳號='ihcaoe', 密碼='aip1614'):
		self.編碼 = 編碼
		self.主機 = 主機
		self.連接埠 = 連接埠
		self.帳號 = 帳號
		self.密碼 = 密碼
	def 剖析物件(self):
		pass
	def 語句剖析後結構化(self):
		pass
	def 語句剖析做語句(self, 語句, 等待=5, 一定愛成功=False):
		# 官方功能無記錄原本換逝資訊，所以愛一逐一擺
		結果 = []
		for 一逝 in 語句.split('\n'):
			愛剖逝 = 一逝.strip()
			if 愛剖逝 == '':
				continue
			while True:
				try:
					剖的結果 = self.連線(愛剖逝, 等待, self.編碼, self.主機, self.連接埠, self.帳號, self.密碼)
					結果.append(剖的結果)
				except Exception as 問題:
					if 一定愛成功:
						print('連線失敗，小等閣試……。原因：{0}'.format(問題),
							file=sys.stderr)
						time.sleep(10)
					else:
						raise
				else:
					break
		print('剖析', 結果)
		return 結果
