'''
Created on 2018年4月12日

@author: pigu
'''
import unittest
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from unittest.case import skip
from 臺灣言語工具.音標系統.閩南語.對照表 import 臺羅對白話字
from _ast import Dict


class 臺羅轉白話字單元試驗(unittest.TestCase):

    def test_大寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Tsui2')
        self.assertEqual(拼音物件.轉白話字(), 'Chuí')

    def test_大寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Tsuí')
        self.assertEqual(拼音物件.轉白話字(), 'Chuí')

    @skip('TODO 待討論')
    def test_大寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('0Tsuí')
        self.assertEqual(拼音物件.轉白話字(), '0Chuí')

    def test_小寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('tshui2')
        self.assertEqual(拼音物件.轉白話字(), 'chhuí')

    def test_小寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('tshuí')
        self.assertEqual(拼音物件.轉白話字(), 'chhuí')

    @skip('TODO 待討論')
    def test_小寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('0tsuí')
        self.assertEqual(拼音物件.轉白話字(), '0chuí')

    def test_韻化輔音m(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('m5').轉白話字(), 'm̂')

    def test_韻化輔音ng(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ng5').轉白話字(), 'n̂g')

    def test_單元音(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('hoo7').轉白話字(), 'hō͘')

    def test_單元音陰入聲(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('hak4').轉白話字(), 'hak')
    
    def test_單元音陽入聲(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('hak8').轉白話字(), 'ha̍k')
    
    def test_單元音入聲鼻音(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('hinnh8').轉白話字(), 'hı̍hⁿ')

    def test_雙元音有i(self):
        # 標佇i以外的元音頂
        self.assertEqual(臺灣閩南語羅馬字拼音('ai5').轉白話字(), 'âi')

    def test_雙元音有i_i在頭前(self):
        # 標佇i以外的元音頂
        self.assertEqual(臺灣閩南語羅馬字拼音('ia5').轉白話字(), 'iâ')

    def test_雙元音無i(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('oa5').轉白話字(), 'ôa')

    def test_雙元音無i_後面的u是u(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('au3').轉白話字(), 'àu')

    def test_雙元音無i_oan(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('uan5').轉白話字(), 'oân')
    
    def test_雙元音無i_oang(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('uang5').轉白話字(), 'oâng')
    
    def test_雙元音無i_nn無算字(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('khuann3').轉白話字(), 'khoaⁿ')
    
    def test_鼻化元音(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('mng5').轉白話字(), 'mn̂g')

    def test_三元音調符_iau(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('iau5').轉白話字(), 'iâu')
    
    def test_三元音調符_oai(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('uai7').轉白話字(), 'oāi')

    def test_三元音調符_nnh(self):
        # TODO: 跟薛確定位置
        self.fail()
        #self.assertEqual(臺灣閩南語羅馬字拼音('uainnh8').轉白話字(), 'ua̍ihⁿ')

    def test_韻對照表(self):
        for 臺羅韻, 白話字韻 in sorted(臺羅對白話字.韻對照表.items()):
            self.assertEqual(臺灣閩南語羅馬字拼音(臺羅韻).轉白話字(), 白話字韻)

#     def test_方言韻(self):
#         self.assertEqual(臺灣閩南語羅馬字拼音('tere5').轉白話字(), 'terê')
#         self.assertEqual(臺灣閩南語羅馬字拼音('tir5').轉白話字(), 'tîr')
#
#     def test_外來語佮輕聲(self):
#         # 符號予別的工具處理
#         self.assertEqual(臺灣閩南語羅馬字拼音('0tir5').轉白話字(), '0tîr')
#         self.assertEqual(臺灣閩南語羅馬字拼音('1tir5').轉白話字(), '1tîr')
