# -*- coding: utf-8 -*-
# @Time    : 2018/1/30
# @Author  : 
# @File    : login_steps.py

from behave import *
import logging

@When("sign out")
def logout(context):
    try:
        # 注销：
        # 依次点击"我"--》"设置"--》"账号管理"--》"账号退出"
        context.execute_steps('''
            When click {0} in {1}
            '''.format("my_profile", "HomePage"))


    except Exception:
        logging.exception("注销过程中出现错误",exc_info=True)
