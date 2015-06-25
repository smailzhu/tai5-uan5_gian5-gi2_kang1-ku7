# -*- coding: utf-8 -*-


def _字陣列揣詞(self, 辭典, 字陣列):
    辭典.查詞 = 辭典.揣詞查詞
    詞組合陣列, 分數, 詞數 = \
            super(self.__class__, self).字陣列揣詞(辭典, 字陣列[::-1])
    辭典.查詞 = 辭典.尾字查詞
    return 詞組合陣列[::-1], 分數, 詞數


def 尾字辭典揣詞(辭典揣詞類):
    return type('尾字{0}'.format(辭典揣詞類.__class__),
            (辭典揣詞類,), {'字陣列揣詞': _字陣列揣詞})
