# -*- coding: utf-8 -*-
# @Time    : 2018/1/28
# @Author  : MaggieTian
# @File    : log_helper.py


import json
import logging.config
import os

'''
加载日志处理配置
'''


class LogHelper:

    # 获取Config目录

    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取项目根目录路径
    config_file_path = os.path.join(project_path, r"Config/")  # 获取Config文件夹路径,所有配置文件都放在config文件夹下

    def __init__(self):
        pass

    @staticmethod
    def setup_logging(default_path='log_config.json', default_level=logging.INFO):
        """Setup logging configuration

        """
        path = default_path
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)









