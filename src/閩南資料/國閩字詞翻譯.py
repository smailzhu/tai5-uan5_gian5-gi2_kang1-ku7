"""
著作權所有 (C) 民國102年 意傳文化科技
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
from 言語資料庫.公用資料 import 標點符號
from 華語台語雙語語料庫系統.文章標點處理工具 import 文章標點處理工具
from 閩南資料.詞 import 詞
from 標音系統整合.標音整合 import 標音整合
from 資料庫工具.型體翻譯 import 型體翻譯

標點處理工具 = 文章標點處理工具()
標點處理工具.標點符號 = 標點符號

def	國閩單位結構化翻譯(型體佮詞性語意):
# 		print(型體佮詞性語意)
	def 提出翻譯資料(資料庫翻譯, 型, 音):
		return [(翻譯[型], 翻譯[音]) for 翻譯 in 資料庫翻譯]
	#####愛徙去別位
	print('翻譯',型體佮詞性語意)
	翻譯集合=[]
	if isinstance(型體佮詞性語意,list) and isinstance(型體佮詞性語意[0],str):
		for 細型體佮詞性語意 in 型體佮詞性語意[1:]:
			print('細型體佮詞性語意=',細型體佮詞性語意)
			細結果集合=國閩單位結構化翻譯(細型體佮詞性語意)[0]
			print('細結果集合',細結果集合)
			翻譯集合.extend(細結果集合)
		return (翻譯集合,型體佮詞性語意[0])

	翻譯集合.append(字音結構化(提出翻譯資料(
		型體翻譯('漢語族官話方言北京官話臺灣腔', 型體佮詞性語意[0], '漢語族閩方言閩南語%'), 7, 8)))

	if 翻譯集合 != [[]]:
		return (翻譯集合,) + tuple(型體佮詞性語意[1:])
	else:
		標音 = 標音整合('漢語族閩方言閩南語')
		音 = 標音.產生標音結果(型體佮詞性語意[0], 標音.文讀層)
		print(型體佮詞性語意[0],'自動標音','=>',音)
		return (音,) + tuple(型體佮詞性語意[1:])

def	國閩單位翻譯(型體佮詞性語意):
# 		print(型體佮詞性語意)
	def 提翻譯(資料庫翻譯, 型, 音):
		return [(翻譯[型], 翻譯[音]) for 翻譯 in 資料庫翻譯]
	#####愛徙去別位
	while isinstance(型體佮詞性語意,list) and isinstance(型體佮詞性語意[0],str):
		型體佮詞性語意=型體佮詞性語意[1]
	翻譯集合 = 提翻譯(型體翻譯('漢語族官話方言北京官話臺灣腔', 型體佮詞性語意[0], '漢語族閩方言閩南語%'), 7, 8)

	return (翻譯集合,) + tuple(型體佮詞性語意[1:])

def 字音結構化(字音結構):
	return [詞(字, 音, 標點處理工具) for 字, 音 in 字音結構]

def 翻譯佮詞性語意字音結構化(翻譯佮詞性語意):
	return (字音結構化(翻譯佮詞性語意[0]),) + tuple(翻譯佮詞性語意[1:])
