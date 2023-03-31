# 1.导包
import unittest
# 2.发现测试目录文件并添加discover('用例所在的路径',’用例代码文件名‘)
suite = unittest.TestLoader().discover('F:\Pychram\pythonProject\case','AceessTo*.py')
#suite = unittest.defaultTestLoader.discover('F:\Pychram\pythonProject\case','AceessTo*.py')
runner = unittest.TextTestRunner()
runner.run(suite)


'''
# 3.使用套件添加用例
def test1():
        suite = unittest.TestSuite()
        suite.addTest(TestDemo('登录后询问权限进入营业区_01'))
        suite.addTest(TestDemo('登录后询问权限进入营业区_01'))
        #suite.addTest(unittest.makeSuite(测试类名))

# 4.实例化运行对象
        runner = unittest.TextTestRunner()
        print('1')
# 5.运行对象
        runner.run(suite)
        print('2')


test1()
'''