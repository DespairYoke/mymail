'''
@Time    : 2018/5/17 20:34
@Author  : Chen Xuge
@Site    : 
@File    : search_indexes.py
@Software: PyCharm
# code is far away from bugs with the god animal protecting
'''

from haystack import indexes
from goods.models import GoodsInfo


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return GoodsInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()