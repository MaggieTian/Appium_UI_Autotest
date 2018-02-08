# -*- coding: utf-8 -*-
# @Time    : 2018/1/21
# @Author  : MaggitTian
# @File    : environment.py

from Util.device import Device
from Util.log_helper import LogHelper
import logging


'''
 在所有feature开始之前连接手机，结束之后断开连接

'''
def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    pass

def before_all(context):
    # 读取配置文件连接手机
    try:
        device = Device()
        device.get_device("device.xml")
        context.driver = device.connect_device('http://localhost:4723/wd/hub')

        # 设置日志配置信息
        LogHelper.setup_logging("log_config.json")
    except Exception:
        logging.exception("连接手机过程中出现错误",exc_info=True)

# 关闭连接
def after_all(context):
    print(context.failed)
    try:
        context.driver.quit()
    except Exception:
        logging.exception("can not quit dirver", exc_info=True)