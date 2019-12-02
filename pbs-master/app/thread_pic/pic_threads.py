# coding =utf-8
import threading,time

class MyThread(threading.Thread):
    """docstring for MyThread"""
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg
      
    def run(self):
        
        print("开始下载图片==="+threading.current_thread().getName())
        time.sleep(2)
        print("OK==="+threading.current_thread().getName())

i = 0
while True:
	i = i+1
	thread = MyThread(str(i))
	thread.start()
	if i%100 == 0:
		time.sleep(5)