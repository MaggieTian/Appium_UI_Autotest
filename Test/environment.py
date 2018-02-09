# -*- coding: utf-8 -*-
# @Time    : 2018/1/21
# @Author  : MaggitTian
# @File    : environment.py

from Util.device import Device
from Util.log_helper import LogHelper
import logging
import os
import csv

'''
 在所有feature开始之前连接手机，结束之后断开连接

'''


def before_feature(context,feature):
    pass

def after_feature(context, feature):
    try:
        row = ['', '', '', '', feature.status]  # 写入feature最终结果
        context.csv.writerow(row)
    except Exception:
        context.logger.exception("after feature 阶段写入csv文件出错",exc_info=True)


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    row = [context.feature.name,scenario.name,scenario.status,",".join(scenario.tags)]
    if context.csv:
        context.csv.writerow(row)


def before_all(context):

    try:
        # 设置logger
        context.logger = LogHelper.set_up_logger()
        # 写入csv Header
        header = ["Feature", "Scenario","Scenario_result","Tags","Result"]
        f_csv = csv.writer(open(os.path.join(LogHelper.root_result,"result.csv"),"w",newline=''))
        f_csv.writerow(header)
        context.csv = f_csv
        # 读取配置文件连接手机
        device = Device()
        device.get_device("device.xml")
        context.device = device.devices   # 传递device信息到后续步骤
        context.driver = device.connect_device('http://localhost:4723/wd/hub') # 所有feature共用一个driver
    except Exception as e:
        print("连接手机过程中出现错误"+str(e))
        context.logger.exception("连接手机过程中出现错误",exc_info=True)

# 关闭连接
def after_all(context):

    # first check there have context.driver
    if context.driver:
        try:
            context.driver.quit()
        except Exception:
            context.logger.exception("can not quit dirver", exc_info=True)

    # 执行后续步骤，生成报告
    ReporterHelper()
