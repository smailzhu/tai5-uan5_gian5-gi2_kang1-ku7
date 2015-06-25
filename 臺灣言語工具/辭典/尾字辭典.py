# -*- coding: utf-8 -*-
from 臺灣言語工具.基本元素.詞 import 詞


def _詞物件反過來(詞物件):
    反過來詞物件 = 詞()
    反過來詞物件.內底字 = 詞物件.內底字[::-1]
    if hasattr(詞物件, '屬性'):
        反過來詞物件.屬性 = 詞物件.屬性
    return 反過來詞物件


def _加詞(self, 詞物件):
    return super(self.__class__, self).加詞(_詞物件反過來(詞物件))


def _頭字查詞(self, 詞物件):
    return super(self.__class__, self).查詞(詞物件)


def _詞組合反過來(結果陣列):
    反過來結果陣列 = []
    for 結果 in 結果陣列:
        反過來結果 = set()
        for 一个詞 in 結果:
            反過來結果.add(_詞物件反過來(一个詞))
        反過來結果陣列.append(反過來結果)
    return 反過來結果陣列


def _尾字查詞(self, 詞物件):
    結果陣列 = self.頭字查詞(_詞物件反過來(詞物件))
    return _詞組合反過來(結果陣列)


def _揣詞查詞(self, 詞物件):
    結果陣列 = self.頭字查詞(詞物件)
    return _詞組合反過來(結果陣列)


def 尾字辭典(辭典類):
    return type('尾字{0}'.format(辭典類.__class__),
            (辭典類,), {'加詞': _加詞, '查詞': _尾字查詞,
                    '頭字查詞': _頭字查詞, '尾字查詞': _尾字查詞, '揣詞查詞': _揣詞查詞})
