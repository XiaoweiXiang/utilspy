# -*- coding:utf-8 -*-
# author: xiaowei xiang

# mutliple sorted
from operator import itemgetter, attrgetter
def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs = sorted(xs, key=attrgetter(key), reverse=reverse)
    return xs
