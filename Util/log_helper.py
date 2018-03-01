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

    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取项目根目录路径
    config_file_path = os.path.join(project_path, "Config"+os.sep)                 # 获取Config文件夹路径,所有配置文件都放在config文件夹下
    root_log_path = os.path.join(project_path,"Log"+os.sep)                        # 获取项目存放Log路径
    root_result = os.path.join(project_path, "Result"+os.sep)                      # 获取存放结果的根目录Result
    root_report = os.path.join(root_result,"Report"+os.sep)                        # 获取存放报告的路径Report
    root_screenshot = os.path.join(root_result,"Screenshot"+os.sep)                # 获取存放截图的路径Screenshot

    @staticmethod
    def setup_logging(default_path='log_config.json', default_level=logging.INFO):

        """Setup logging configuration

        """
        path = os.path.join(LogHelper.config_file_path, default_path)  # 得到配置文件的绝对路径
        if os.path.exists(path):
            try:
                with open(path, 'rt') as f:
                    config = json.load(f)
                logging.config.dictConfig(config)

            except Exception:
                logging.exception("读取日志配置文件出错",exc_info=True)

        else:
            logging.basicConfig(level=default_level)

    @staticmethod
    def set_up_logger():
        '''
        配置logger
        :return: logger
        '''

        logger = logging.getLogger("output")
        formater = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        # 每次重新运行feature配置时都会覆盖原来的日志
        file_handler = logging.FileHandler(os.path.join(LogHelper.root_log_path,"output.log"),'w',encoding="utf-8")
        file_handler.setFormatter(formater)
        file_handler.setLevel(logging.ERROR)    # 设置输出日志只记录错误信息
        logger.addHandler(file_handler)
        return logger

# Debug
if __name__ == "__main__":

    print(LogHelper.config_file_path)









