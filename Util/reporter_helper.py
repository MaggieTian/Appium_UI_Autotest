#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/9
# @Author  : MaggieTian
# @File    : reporter_helper.py
import csv
from Util.log_helper import LogHelper
import os
import xlwt

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


class ReporterHelper:

    # 保存所以Feature运行结果的excel文件表头
    TABLE_HEAD = ['Feature', 'Scenario', 'Scenario_Result', 'Tag', 'Result']
    ROW = 1  # 行
    COL = 0  # 列

    def __init__(self,result_file,device = None):
        self.result_file = result_file
        self.device = device

    def generate_report(self,template_html):
        pass

    def generate_detail_table(self):
        pass

    @staticmethod
    def get_excel_table():
        workbook = xlwt.Workbook("utf-8")                                   # 新建工作簿
        worksheet = workbook.add_sheet("result", cell_overwrite_ok=True)     # 新建sheet
        for i in range(0, len(ReporterHelper.TABLE_HEAD)):
            worksheet.write(0, i, ReporterHelper.TABLE_HEAD[i])                            # 写入表头
        return worksheet, workbook

# debug
if __name__ =='__main__':
    result = ReporterHelper(os.path.join(LogHelper.root_result,"result.csv")).generate_detail_table()
    print(result)

