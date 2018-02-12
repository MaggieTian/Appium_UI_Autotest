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
RUN_DATE='''<h3 align="center"执行日期：>{date}</h3><br>'''.format(date=time.localtime(time.time()))

# 测试汇总情况说明表
TOTAL_TABLE = '''
<!--<div class="container">-->
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div class="row">
        <div class="col-md-4 col-md-offset-2" id="main" style="width: 600px;height:400px;" align="center"></div>
        <div class="col-md-2 col-md-offset-2">
            <table class="table table-striped">
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
        self.scenario = {'cnt': 0, 'result': []}

    def generate_report(self, template_html):

        # 生成total和detail的table和数据
        detail = self.generate_detail_table()
        total = self.generate_total_table()
        index_html = open(os.path.join(LogHelper.root_result,"index.html"),"w")
        with open(template_html,"r") as f:
            for line in f:
                if line.find("<body>"):
                    index_html.write(TOTAL_TABLE)
                    for i in total:
                        index_html.write(i)
                    for j in detail:
                        index_html.write(j)
                else:
                    index_html.write(line)



    def generate_total_table(self):
        if self.device:
            for key,value in self.device.items():
                yield "<tr><td>{key}</td><td>{value}</td></tr>".format(key=key,value=value)

            total = "<tr><td>{feature}</td><td>{cnt}</td></tr>".format(feature="Feature总计",cnt=str(self.feature['cnt']))
            total += "<tr><td>{scenario}</td><td>{s_cnt}</td></tr>".format(scenario="scenario总计",s_cnt=str(self.scenario['cnt']))
            yield total+"</div></div></table>"
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
                    self.scenario['result'].append(row_values.Scenario_Result)

                decrate = "<tr>"
                if row_values.Scenario_Result == 'passed':
                    decrate = "<tr class='success'>"
                elif row_values.Scenario_Result == "failed":
                    decrate = "<tr class='danger'>"
                yield decrate + "<td>{feature}</td><td>{scenario}</td><td>{scenario_result}</td><td>{tag}</td><td>{result}</td></tr>".\
                    format(feature=row_values.Feature, scenario=row_values.Scenario, scenario_result=row_values.Scenario_Result,tag= row_values.Tag, result=row_values.Result)
            yield "</table>"
        else:
            logger.error("测试结果文件不存在！")


    @staticmethod
    def get_excel_table():
        workbook = xlwt.Workbook("utf-8")                                   # 新建工作簿
        worksheet = workbook.add_sheet("result", cell_overwrite_ok=True)     # 新建sheet
        for i in range(0, len(ReporterHelper.TABLE_HEAD)):
            worksheet.write(0, i, ReporterHelper.TABLE_HEAD[i])                            # 写入表头
        return worksheet, workbook

# debug
if __name__ =='__main__':

    report = ReporterHelper(os.path.join(LogHelper.root_result,"result.xls"),device={'platformName': 'Android', 'platformVersion': '5.1', 'deviceName': '58b9f28a7d52', 'appPackage': 'com.sina.weibo'})
    data = report.generate_total_table()
    for i in data:
        print(i)

