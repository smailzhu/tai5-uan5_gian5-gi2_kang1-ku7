# -*- coding: utf-8 -*-
import os
from 臺灣言語工具.語音合成.語音標仔轉換 import 語音標仔轉換
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from 臺灣言語工具.語音辨識.語料處理 import 語料處理


class 辨識模型(程式腳本, 語料處理):
    _轉合成標仔 = 語音標仔轉換()
    恬音 = _轉合成標仔.提出標仔主要音值(_轉合成標仔.恬音)
    短恬 = _轉合成標仔.提出標仔主要音值(_轉合成標仔.短恬)

    def 對齊(self, 參數檔, 聲韻類檔, 對照檔, 模型檔,
                    標仔檔, 特徵檔, 結果夾, 執行檔路徑=''):
        執行檔路徑 = self._執行檔路徑加尾(執行檔路徑)
        os.makedirs(結果夾, exist_ok=True)
        對齊指令 = '{0}HVite -A -C {1} -p -20 -H {2} -I {3} -S {4} -o S -y lab -l "{5}" {6} {7}'\
                .format(執行檔路徑, 參數檔, 模型檔, 標仔檔, 特徵檔,
                        結果夾, 對照檔, 聲韻類檔)
        self._走指令(對齊指令)
        return

    def 對齊聲韻(self, 聲韻類檔, 模型檔, 聲韻檔, 特徵檔, 資料目錄, 執行檔路徑=''):
        參數檔 = os.path.join(資料目錄, '參數檔.cfg')
        self.設定參數(聲韻類檔, 參數檔)
        聲韻對照檔 = os.path.join(資料目錄, '聲韻對照檔.dict')
        self.家己對照檔(聲韻類檔, 聲韻對照檔)
        對齊結果檔 = os.path.join(資料目錄, '對齊聲韻結果')
        self.對齊(參數檔, 聲韻類檔, 聲韻對照檔, 模型檔, 聲韻檔, 特徵檔, 對齊結果檔, 執行檔路徑)
        return 對齊結果檔

    def 對齊音節(self, 音節聲韻對照檔, 聲韻類檔, 模型檔, 音節檔, 特徵檔, 資料目錄, 執行檔路徑=''):
        參數檔 = os.path.join(資料目錄, '參數檔.cfg')
        self.設定參數(聲韻類檔, 參數檔)
        對齊結果檔 = os.path.join(資料目錄, '對齊音節結果')
        self.對齊(參數檔, 聲韻類檔, 音節聲韻對照檔, 模型檔, 音節檔, 特徵檔, 對齊結果檔, 執行檔路徑)
        return 對齊結果檔

    def 辨識(self, 設定檔, 聲韻類檔, 對照檔, 模型檔, 網路檔, 幾條網路, 特徵檔, 結果檔, 結果網路資料夾, 執行檔路徑=''):
        執行檔路徑 = self._執行檔路徑加尾(執行檔路徑)
        if 幾條網路 > 0:
            os.makedirs(結果網路資料夾, exist_ok=True)
            幾條網路設定 = '-n {0}'.format(幾條網路)
        else:
            結果網路資料夾 = '*'
            幾條網路設定 = ''
        辨識指令 = '{0}HVite -A -C {1} -p -20 -H {2} -w {3} -S {4} -o N -y rec -z lattices -i {5} -l "{6}" {7} {8} {9}'\
                .format(執行檔路徑, 設定檔, 模型檔, 網路檔, 特徵檔,
                        結果檔, 結果網路資料夾, 幾條網路設定, 對照檔, 聲韻類檔)
        self._走指令(辨識指令)
        return

    def 辨識聲韻(self, 聲韻類檔, 模型檔, 特徵檔, 資料目錄, 幾條網路, 執行檔路徑=''):
        參數檔 = os.path.join(資料目錄, '參數檔.cfg')
        self.設定參數(聲韻類檔, 參數檔)
        網路檔 = os.path.join(資料目錄, '聲韻網路檔.lat')
        self.生辨識網路(執行檔路徑, 資料目錄, 聲韻類檔, 網路檔)
        結果檔 = os.path.join(資料目錄, '辨識聲韻結果檔.mlf')
        聲韻對照檔 = os.path.join(資料目錄, '聲韻對照檔.dict')
        self.家己對照檔(聲韻類檔, 聲韻對照檔)
        結果網路資料夾 = os.path.join(資料目錄, '辨識聲韻網路')
        self.辨識(參數檔, 聲韻類檔, 聲韻對照檔, 模型檔, 網路檔, 幾條網路,
                特徵檔, 結果檔, 結果網路資料夾, 執行檔路徑)
        return 結果檔, 結果網路資料夾

    def 辨識音節(self, 音節聲韻對照檔, 聲韻類檔, 模型檔,
                    特徵檔, 資料目錄, 幾條網路, 執行檔路徑=''):
        參數檔 = os.path.join(資料目錄, '參數檔.cfg')
        self.設定參數(聲韻類檔, 參數檔)
        音節類檔 = os.path.join(資料目錄, '音節類檔.list')
        self.家己類檔(音節聲韻對照檔, 聲韻類檔, 音節類檔)
        網路檔 = os.path.join(資料目錄, '音節網路檔.lat')
        self.生辨識網路(執行檔路徑, 資料目錄, 音節類檔, 網路檔)
        結果檔 = os.path.join(資料目錄, '辨識音節結果檔.mlf')
        結果網路資料夾 = os.path.join(資料目錄, '辨識音節網路')
        self.辨識(參數檔, 聲韻類檔, 音節聲韻對照檔, 模型檔, 網路檔, 幾條網路,
                特徵檔, 結果檔, 結果網路資料夾, 執行檔路徑)
        return 結果檔, 結果網路資料夾

    def 處理試驗語料(self, 音檔目錄, 資料目錄,
                    標仔目錄=None, 音節聲韻對照檔=None, 執行檔路徑=''):
        全部語料 = self.揣全部語料(音檔目錄, 標仔目錄)
        全部特徵檔 = os.path.join(資料目錄, '資料特徵檔.scp')
        os.makedirs(資料目錄, exist_ok=True)
        self.揣特徵而且算(執行檔路徑, 資料目錄, 全部語料, 全部特徵檔)
        if 標仔目錄 is None:
            return 全部特徵檔
        全部標仔檔 = os.path.join(資料目錄, '試驗語料標仔檔.scp')
        音節檔 = os.path.join(資料目錄, '試驗語料音節檔.mlf')
        聲韻類檔 = os.path.join(資料目錄, '試驗語料聲韻類檔.list')
        聲韻檔 = os.path.join(資料目錄, '試驗語料聲韻檔.mlf')
        全部標仔 = []
        for 語料 in 全部語料:
            標仔所在 = 語料[2]
            全部標仔.append(標仔所在)
        self._陣列寫入檔案(全部標仔檔, 全部標仔)
        用袂著的檔案 = os.path.join(資料目錄, '用袂著的檔案.garbage')
        self.標仔收集起來(執行檔路徑, 全部標仔檔, 資料目錄, 用袂著的檔案, 音節檔)
        self.標仔切做聲韻(執行檔路徑, 音節檔, 音節聲韻對照檔, 資料目錄, 聲韻類檔, 聲韻檔)
# 		self.標仔加恬佮切開(執行檔路徑, 全部標仔檔, 音節聲韻對照檔,
# 			資料目錄, 音節檔, 聲韻類檔, 聲韻檔)
        return 全部特徵檔, 音節檔, 聲韻檔

    def 生辨識網路(self, 執行檔路徑, 資料目錄, 聲韻類檔, 網路檔):
        執行檔路徑 = self._執行檔路徑加尾(執行檔路徑)
        辨識的可能 = set()
        短恬語法 = ''
        for 聲韻 in self._讀檔案(聲韻類檔):
            主要音值 = self._轉合成標仔.提出標仔主要音值(聲韻)
            if 主要音值 == self.短恬:
                短恬語法 = '[{0}]'.format(self.短恬)
            elif 主要音值 == self.恬音:
                pass
            else:
                辨識的可能.add(主要音值)
        語法 = '{2}={3};\n({0} < {2} {1} > {0})'.format(
                self.恬音, 短恬語法,
                '$SYL', '|'.join(辨識的可能))
        語法檔 = os.path.join(資料目錄, '語法檔.syntax')
        self._字串寫入檔案(語法檔, 語法)
        產生網路指令 = '{0}HParse -A {1} {2}'\
                .format(執行檔路徑, 語法檔, 網路檔)
        self._走指令(產生網路指令)

    def 家己類檔(self, 對照檔, 聲韻類檔, 類檔):
        聲韻類 = set()
        for 聲韻 in self._讀檔案(聲韻類檔):
            聲韻類.add(self._轉合成標仔.提出標仔主要音值(聲韻))
        類表 = []
        for 類 in self._讀檔案(對照檔):
            音節, *拆聲韻 = 類.split()
            for 聲韻 in 拆聲韻:
                if 聲韻 not in 聲韻類:
                    break
            else:
                類表.append('{0}'.format(音節))
        self._陣列寫入檔案(類檔, 類表)

    def 家己對照檔(self, 類檔, 對照檔):
        對照表 = []
        for 類 in self._讀檔案(類檔):
            對照表.append('{0}\t{0}'.format(
                    self._轉合成標仔.提出標仔主要音值(類)))
        self._陣列寫入檔案(對照檔, set(對照表))

    def 設定參數(self, 聲韻類檔, 上尾參數檔):
        參數 = ['noNumEscapes = TRUE']
        if '-' in ''.join(self._讀檔案(聲韻類檔)):
            參數.append('ALLOWXWRDEXP = TRUE')
            參數.append('FORCECXTEXP = TRUE')
        self._陣列寫入檔案(上尾參數檔, 參數)
