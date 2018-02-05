# -*- coding: utf-8 -*-
# @Time    : 2018/1/23
# @Author  : MaggieTian
# @File    : check.py
from Util.locate_helper import LocateHeper
import logging
from Util.map import _Page_Map

'''
验证传入的page参数是否在映射关系中
'''


def check_page(page):
    if page in _Page_Map.keys():
        return _Page_Map[page]()  # 能在page_map中找到相应的映射关系就返回page对象
    else:
        msg = "{page} not in page map".format(page=page)  # 打印并抛出异常
        raise Exception(msg)


