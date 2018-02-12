# -*- coding: utf-8 -*-
# @Time    : 2018/1/21
# @Author  : MaggitTian
# @File    : environment.py

from Util.device import Device
from Util.log_helper import LogHelper
import os
from Util.reporter_helper import ReporterHelper


'''
 在所有feature开始之前连接手机，结束之后断开连接

'''

def before_feature(context,feature):
    try:
        context.worksheet.write(ReporterHelper.ROW,ReporterHelper.COL, feature.name)
        context.feature_row = ReporterHelper.ROW
    except:
        context.logger.exception("write in excel in before_feature steps happend exception",exc_info= True)


def after_feature(context, feature):
    try:
        context.worksheet.write(context.feature_row,ReporterHelper.COL+len(ReporterHelper.TABLE_HEAD)-1, feature.status)
    except:
        context.logger.exception("write in excel in after_feature steps happend exception",exc_info= True)


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):

    # 分别写入scenario.name、scenario.status、scenario.tags
    try:
        for col,vaule in zip(list(range(1,len(ReporterHelper.TABLE_HEAD)-1)),[scenario.name,scenario.status,",".join(scenario.tags)]):
            context.worksheet.write(ReporterHelper.ROW , col, vaule)
        ReporterHelper.ROW += 1  # 每运行一个scenario行数+1

    except Exception:
        context.logger.exception("write in excel in after_scenario steps happend exception",exc_info= True )


def before_all(context):

    try:
        # 设置logger
        context.logger = LogHelper.set_up_logger()
        # 设置写入结果信息的excel工作簿
        context.worksheet, context.workbook = ReporterHelper.get_excel_table()
        # 读取配置文件连接手机
        device = Device()
        device.get_device("device.xml")
        context.device = device.devices   # 传递device信息到后续步骤
        context.driver = device.connect_device('http://localhost:4723/wd/hub') # 所有feature共用一个driver
    except Exception as e:
        context.logger.exception("连接手机过程中出现错误", exc_info=True)

# 关闭连接
def after_all(context):

    # first check there have context.driver
    if context.driver:
        try:
            context.driver.quit()
        except Exception:
            context.logger.exception("can not quit driver", exc_info=True)
    # save the result excel file
    if context.workbook:
        try:
            context.workbook.save(os.path.join(LogHelper.root_result, "result.xls"))
        except Exception:
            context.logger.exception("save the result excel file happened exception",exc_info = True)

    # 执行后续步骤，生成报告
    # ReporterHelper()
