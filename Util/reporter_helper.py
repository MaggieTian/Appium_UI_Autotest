#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/9
# @Author  : MaggieTian
# @File    : reporter_helper.py
import csv
from Util.log_helper import LogHelper
import logging
import os
import xlwt
import xlrd
from collections import namedtuple
import time

# 生成详情表格的table
DETAIL_TABLE = '''<table id= "detail" border="4" align="center" class="table table-condensed">
            <tr>
            <th>Feature</th>
            <th>Scenario</th>
            <th>Scenario Result</th>
            <th>Tag</th>
            <th>Result</th>
        </tr>
'''
# 报告标题
REPORT_TITLE = '''<h1 align="center">{title}</h1><br>'''.format(title="***** **** Test  Detail Report")

# 执行日期
RUN_DATE='''<h3 align="center"执行日期：>{date}</h3><br>'''.format(date=time.strftime('%Y/%m/%d %A',time.localtime(time.time())))

# 设备信息说明表
DEVICE_TABLE = '''
<!--<div class="container">-->
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div class="row">
        <div class="col-md-4 col-md-offset-2" id="main" style="width: 600px;height:400px;" align="center"></div>
        <div class="col-md-2 col-md-offset-2">
        <p align="center"><b>设备信息</b></p>
            <table class="table table-striped">
'''
# 测试结果汇总情况
TOTAL_DIV = '''
<div class="row">
    <div class="col-md-1 col-md-offset-10"><span style="background-color:green"><b>Scenario成功：{suc_cnt}</b></span></div>
    <div class="col-md-1"><span style="background-color:red"><b>Scenario失败：{fail_cnt}</b></span></div>
</div>
'''

logger = logging.getLogger("output")
class ReporterHelper:

    # 保存所以Feature运行结果的excel文件表头
    TABLE_HEAD = ['Feature', 'Scenario', 'Scenario_Result', 'Tag', 'Result']
    ROW = 1  # 行
    COL = 0  # 列

    def __init__(self,result_file,device = None):
        self.result_file = result_file
        self.device = device

        # 用来记录feature和scenario执行情况
        self.feature = {'cnt': 0, 'result': []}
        self.scenario = {'cnt': 0, 'suc_cnt': 0, 'fail_cnt': 0}

    def generate_report(self, template_html):

        # 生成total和detail的table和数据。
        detail = self.generate_detail_table()
        total = self.generate_total_table()
        index_html = open(os.path.join(LogHelper.root_report,"index.html",), "w", encoding="utf-8")
        with open(template_html,"r", encoding="utf-8") as f:
            for line in f:
                if line.find("<body>") > -1:                      # 找到<body>标签，在该标签之后写入测试结果数据
                    index_html.write(REPORT_TITLE)                # 写入报告标题
                    index_html.write(RUN_DATE)                    # 写入执行日期
                    index_html.write(DEVICE_TABLE)                 # 写入总体测试结果
                    for i in total:
                        index_html.write(i)
                    index_html.write(DETAIL_TABLE)                # 写入详细测试结果
                    for j in detail:
                        index_html.write(j)
                if line.find("passed_cnt") > -1:
                    line.replace("passed_cnt",str(self.scenario['suc_cnt']))
                if line.find("failed_cnt")> -1:
                    line.replace("failed_cnt",str(self.scenario['fail_cnt']))
                index_html.write(line)

    #  根据device信息生成表格信息
    def generate_total_table(self):
        if self.device:
            for key,value in self.device.items():
                yield "<tr><td>{key}</td><td>{value}</td></tr>\n".format(key=key,value=value)
            yield "</table></div></div>\n"
        else:
            logger.error("there is no device info!")

    def generate_detail_table(self):

        if os.path.exists(self.result_file):
            data = xlrd.open_workbook(self.result_file)           # 打开excel文件
            table = data.sheets()[0]                              # 得到表格
            nrows = table.nrows
            Row = namedtuple("Row", table.row_values(0))
            for i in range(1, nrows):
                row_values = Row(*(table.row_values(i)))          # 获取某一行数据,使用命名元组，避免使用索引获取内容
                if row_values.Feature!= ''and row_values.Result!= '':
                    self.feature['cnt'] +=1
                    self.feature['result'].append(row_values.Result)
                if row_values.Scenario != '' and row_values.Scenario_Result !='':
                    self.scenario['cnt'] += 1

                decrate = "<tr>"
                if row_values.Scenario_Result == 'passed':
                    decrate = "<tr class='success'>"
                    self.scenario['suc_cnt'] +=1
                elif row_values.Scenario_Result == "failed":
                    decrate = "<tr class='danger'>"
                    self.scenario['fail_cnt'] += 1
                yield decrate + "<td>{feature}</td><td>{scenario}</td><td>{scenario_result}</td><td>{tag}</td><td>{result}</td></tr>\n".\
                    format(feature=row_values.Feature, scenario=row_values.Scenario, scenario_result=row_values.Scenario_Result,tag= row_values.Tag, result=row_values.Result)
            yield "</table>\n"
            yield TOTAL_DIV.format(suc_cnt=self.scenario['suc_cnt'], fail_cnt=self.scenario['fail_cnt'])
        else:
            logger.error("测试结果文件不存在！")


    @staticmethod
    def get_excel_table():
        workbook = xlwt.Workbook("utf-8")                                                   # 新建工作簿
        worksheet = workbook.add_sheet("result", cell_overwrite_ok=True)                    # 新建sheet
        for i in range(0, len(ReporterHelper.TABLE_HEAD)):
            worksheet.write(0, i, ReporterHelper.TABLE_HEAD[i])                             # 写入表头
        return worksheet, workbook

# debug
if __name__ =='__main__':

    report = ReporterHelper(os.path.join(LogHelper.root_result,"result.xls"),device={'platformName': 'Android', 'platformVersion': '5.1', 'deviceName': '58b9f28a7d52', 'appPackage': 'com.sina.weibo'})
    report.generate_report(os.path.join(LogHelper.root_report, "template.html"))

