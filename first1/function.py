from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMessageBox, QMainWindow
from first import Ui_MainWindow


# test_mian 类又提供了一个容器，这个类继承自QMainWindow,Ui_MainWindow，
# 在这个类的构造函数中运行类父类的构造函数，并且把它自己作为参数产地给setupUi，并且添加了信号&槽信息
# 初始化设置。init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 解释器会自动调用该函数，且不用传递该参数
class test_mian(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)  # 初始化继承的父类。QMainWindow为Pyqt5的基本控件
        Ui_MainWindow.__init__(self)  # 初始化继承的父类。
        self.setupUi(self)  # 调用Ui_MainWindow类中的setupUi函数
        self.pushButton.clicked.connect(self.btn_change1)   # 使得信号与槽函数进行手工绑定，pushButton为控件名称
        self.pushButton_2.clicked.connect(self.btn_change2)  # 使得信号与槽函数进行手工绑定，pushButton_2为控件名称

    def btn_change1(self):
        self.textEdit.setText('世界，我来了！')

    def btn_change2(self):
        self.textEdit.setText('哈哈哈哈哈哈哈哈哈！')
