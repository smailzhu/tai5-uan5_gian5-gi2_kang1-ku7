# -*- coding: utf-8 -*-
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞


class 上長詞優先辭典揣詞(拄好長度辭典揣詞):
    def 字陣列揣詞(self, 辭典, 字陣列):
        if hasattr(辭典, '空'):
            字陣列 = self.字陣列改數字(辭典, 字陣列)
        詞組合陣列 = []
        詞數量 = 0
        所在 = 0
        while 所在 < len(字陣列):
            愛查的字 = 字陣列[所在:所在 + 辭典.上濟字數()]
            查著的詞 = 辭典.查詞(詞(愛查的字))
            for 字數, 查著的 in\
                    zip(range(len(愛查的字), 0, -1), 查著的詞[::-1]):
                if len(查著的) > 0:
                    這擺詞長度 = 字數
                    詞組合 = 查著的
                    break
            else:
                這擺詞長度 = 1
                詞物件 = 詞([字陣列[所在]])
                詞物件.屬性 = {'無佇辭典': True}
                詞組合 = {詞物件}
            詞組合陣列.append(詞組合)
            所在 += 這擺詞長度
            詞數量 += 1
        return 詞組合陣列, -0.0, 詞數量
