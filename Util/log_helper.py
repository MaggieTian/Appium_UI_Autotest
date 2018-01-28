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
    def __init__(self):
        pass

    def setup_logging(self, default_path='log_config.json', default_level=logging.INFO):
        """Setup logging configuration

        """
        path = default_path
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)