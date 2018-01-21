# -*- coding: utf-8 -*-
# @Time    : 2018/1/21
# @Author  : MaggitTian
# @File    : environment.py

from Util.device import Device
import os

'''
 在所有feature开始之前连接手机，结束之后断开连接

'''


def before_all(context):

    # 读取配置文件连接手机
    device = Device()
    device.get_device("device.xml")
    context.driver = device.connect_device('http://localhost:4723/wd/hub')

# 关闭连接
def after_all(context):

    context.driver.quit()