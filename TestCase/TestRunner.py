import unittest
import os
import sys
import time
from datetime import datetime
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

print(os.path.dirname(os.path.abspath(__file__)) + '/../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
test_dir = "../TestCase"

now_time = str(datetime.now().strftime("%Y-%m-%d")) + '-'+str(time.time())

report_path = 'F:/Pychram/pythonProject/TestReport/' + now_time + '.html'

file_path = open(report_path,"w")

discover = unittest.TestLoader().discover(test_dir,'test_*.py')

#runner = unittest.TextTestRunner()
runner = HTMLTestRunner(stream=file_path)

runner.run(discover)

file_path.close()
