import logging
import time
import os.path


class logger():
    def __init__(self,logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handle，写入日志文件
        rt=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        '''
        以下实例展示了 time() 函数的使用方法：

        #!/usr/bin/python
        import time
        
        print "time.time(): %f " %  time.time()
        print time.localtime( time.time() )
        print time.asctime( time.localtime(time.time()) )
        以上实例输出结果为：
        
        time.time(): 1234892919.655932
        (2009, 2, 17, 10, 48, 39, 1, 48, 0)
        Tue Feb 17 10:48:39 2009
        '''

        log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/logs/'
        log_name = log_path + rt + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
