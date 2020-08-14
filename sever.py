# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2019/9/25 9:57 AM

# File_name: 'app_case_analysis.py'

"""
Describe: this is a demo!
"""
import traceback
import logging.config


from os import path
from src.parsing_response import parsing_response
from src.manger import manger
import time
from flask import Flask, request, jsonify



import json
# 导入日志配置文件
log_file_path = path.join(path.dirname(path.abspath(__file__)),"./configs/logging.conf")
print(log_file_path)
logging.config.fileConfig(log_file_path)
# 创建日志对象
logger = logging.getLogger()
loggerInfo = logging.getLogger("TimeInfoLogger")
Consolelogger = logging.getLogger("ConsoleLogger")
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/consult", methods=["POST"])
def consult():
    res = request.get_json(force=True)
    # 获取uuid
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('当前时间: ', current_time)
    logger.info("res type::%s" % type(res))
    try:
        # 返回最终动态文件内容
        data_list,user_key_words,uuid = parsing_response(res)
        print(len(data_list))
        result = manger(data_list,user_key_words,uuid)
        print("正确")
        logger.info("result code:%s" % '200')
        return jsonify(result)
    except:
        print('异常')
        print(traceback.format_exc())
        return jsonify({'code': '400'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)
