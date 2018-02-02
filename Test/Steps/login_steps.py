# -*- coding: utf-8 -*-
# @Time    : 2018/1/30
# @Author  : 
# @File    : login_steps.py

from behave import *


@When("sign out")
def logout(context):
        # 注销：
        # 依次点击"我"--》"设置"--》"账号管理"--》"账号退出"
        context.execute_steps('''
            When click {0} in {1}
            '''.format("setting", "SettingPage"))
        context.execute_steps(
            '''
            When click {0} in {1}
            And waiting for {2} seconds
            '''.format("accout_manage","SettingPage",5))
        context.execute_steps(
            '''
            Then there should be {0} in {1}
            '''.format("exit_accout","SettingPage")
        )
        context.execute_steps(
            '''
            When click {0} in {1}
            And waiting for {2} seconds
            Switch to alert window and click {3} in {4}
            And waiting for {5} seconds
            '''.format("exit_accout", "SettingPage", 5, "sure", "SettingPage", 3)
        )
