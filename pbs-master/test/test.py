import sys
sys.path.append('..')
from log.log import get_loger
import logging

log = get_loger("gen.txt",logging.ERROR)
def testLogHandler():
    log.critical('critical级别的信息')
    log.error('error级别的信息')
    log.warning('warning级别的信息')
    log.info('info级别的信息')
    log.debug('debug级别的信息')


if __name__ == '__main__':
    testLogHandler()
