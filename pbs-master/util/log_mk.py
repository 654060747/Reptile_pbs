#coding=utf-8
# # # # # # # # BEGIN INIT INFO # # # # # # # # # # # # # #
#  copyright   : Copyright (c) 2019 xxx.
#  filename    : log.py
#  author      : xxx/data.dev
#  version     : 0.0.1
#  created     : 2019-08-17
#  description : 打印日志
#
#  history     :
#
# # # # # # # # END INIT INFO # # # # # # # # # # # # # # #

import logging,os
from logging.handlers import TimedRotatingFileHandler

# debug(调试信息) < info(一般信息) < warning(警告信息) < error(错误信息) < critical(致命信息),从左往右越来越严重
# 默认为debug级别，即大于等于的级别的日志才输出
# 日志输出格式为：输出日期 使用到日志文件 第几行打印的日志 日志级别：设置的打印信息
# 日志文件统一保存在上一级logs目录 
    
# 参数： 
#   log_save_file：log日志保存的文件名(一般使用.log后缀文件保存,当然也可以使用.txt等)
#           level：日志级别,默认为DEBUG级别 
# 返回值: logger对象

# 当前路径
current_path = os.path.dirname(os.path.abspath(__file__))
# 当前路径上级目录
up_path = os.path.join(current_path, os.pardir)
# 日志统一保存目录logs
log_save_path = os.path.join(up_path, 'logs')

def check_dir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass

check_dir(log_save_path)

def get_loger(log_save_file, level=logging.DEBUG):
    # 创建一个logger
    logger = logging.getLogger(log_save_file)
    # 设置日志级别
    logger.setLevel(level)
    # 定义输出格式
    output_format = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s:%(message)s')

    # 创建文件处理器,将日志输出到文件
    file_name = os.path.join(log_save_path,log_save_file)
    # 日志目录下超过15个日志文件就会丢弃掉老的日志文件,时间间隔2天
    file_handler = TimedRotatingFileHandler(filename=file_name,when='D',interval=2,backupCount=15,encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.setFormatter(output_format)
    # 给logger添加处理器
    logger.addHandler(file_handler)

    # 创建终端输出处理器,将日志输出到终端
    terminal_handler = logging.StreamHandler()
    terminal_handler.setFormatter(output_format)
    logger.addHandler(terminal_handler)

    return logger

# 测试
def test_print_log():
    # 如果设置ERROR级别,小于ERROR级别日志不会输出
    log = get_loger('test.log',logging.ERROR)
    log.critical('critical级别的信息')
    log.error('error级别的信息')
    log.warning('warning级别的信息')
    log.info('info级别的信息')
    log.debug('debug级别的信息')


if __name__ == '__main__':
    test_print_log()