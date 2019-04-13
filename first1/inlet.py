import sys
from PyQt5 import QtWidgets
from function import test_mian

if __name__ == "__main__":  # 用于判断是否直接运行.py文件
    app = QtWidgets.QApplication(sys.argv)  # 实例化QApplication类，作为GUI主程序入口，需要import sys，可紧放在这句之前，也可放在代码最前面部分
    mywindow = test_mian()  # 实例化之前定义的窗口类
    mywindow.show()  # 使用 show() 方法
    sys.exit(app.exec_())