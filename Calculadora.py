# Form implementation generated from reading ui file 'Calculadora.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        Calculadora.setObjectName("Calculadora")
        Calculadora.resize(488, 652)
        Calculadora.setStyleSheet("background-color: rgb(61, 61, 61);")
        self.centralwidget = QtWidgets.QWidget(Calculadora)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(470, 634))
        self.frame.setMaximumSize(QtCore.QSize(470, 634))
        self.frame.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"background-color: rgb(33, 33, 33);\n"
"border-radius: 4px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 451, 81))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: ;\n"
"    background-color: qlineargradient(spread:reflect, x1:0.48, y1:0.539773, x2:0.485921, y2:0.983, stop:0 rgba(194, 204, 145, 255), stop:0.837079 rgba(158, 166, 118, 255));\n"
"    border: 2px solid rgb(63, 63, 63);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.display_1 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.display_1.setFont(font)
        self.display_1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.display_1.setStyleSheet("border: none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.display_1.setText("")
        self.display_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.display_1.setObjectName("display_1")
        self.verticalLayout.addWidget(self.display_1)
        self.display_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.display_2.setFont(font)
        self.display_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.display_2.setStyleSheet("border: none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.display_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.display_2.setObjectName("display_2")
        self.verticalLayout.addWidget(self.display_2)
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 100, 451, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_mp = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_mp.setFont(font)
        self.btn_mp.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_mp.setObjectName("btn_mp")
        self.gridLayout.addWidget(self.btn_mp, 2, 3, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 1, 3, 1, 1)
        self.btn_fp = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_fp.setFont(font)
        self.btn_fp.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_fp.setObjectName("btn_fp")
        self.gridLayout.addWidget(self.btn_fp, 0, 1, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_pc = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_pc.setFont(font)
        self.btn_pc.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_pc.setObjectName("btn_pc")
        self.gridLayout.addWidget(self.btn_pc, 0, 2, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_ap = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_ap.setFont(font)
        self.btn_ap.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_ap.setObjectName("btn_ap")
        self.gridLayout.addWidget(self.btn_ap, 0, 0, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_menos = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_menos.setFont(font)
        self.btn_menos.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_menos.setObjectName("btn_menos")
        self.gridLayout.addWidget(self.btn_menos, 3, 3, 1, 1)
        self.btn_ac = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_ac.setFont(font)
        self.btn_ac.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_ac.setObjectName("btn_ac")
        self.gridLayout.addWidget(self.btn_ac, 0, 3, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 1)
        self.btn_ponto = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_ponto.setFont(font)
        self.btn_ponto.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_ponto.setObjectName("btn_ponto")
        self.gridLayout.addWidget(self.btn_ponto, 4, 1, 1, 1)
        self.btn_igual = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_igual.setFont(font)
        self.btn_igual.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(222, 36, 45);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(188, 31, 39);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(188, 31, 39);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_igual.setObjectName("btn_igual")
        self.gridLayout.addWidget(self.btn_igual, 4, 2, 1, 1)
        self.btn_mais = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_mais.setFont(font)
        self.btn_mais.setStyleSheet("QPushButton{    \n"
"    height: 90px;\n"
"    background-color: rgb(136, 136, 136);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 85);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 4px solid rgba(0, 0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.btn_mais.setObjectName("btn_mais")
        self.gridLayout.addWidget(self.btn_mais, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(16, 609, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.frame)
        Calculadora.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculadora)
        QtCore.QMetaObject.connectSlotsByName(Calculadora)

    def retranslateUi(self, Calculadora):
        _translate = QtCore.QCoreApplication.translate
        Calculadora.setWindowTitle(_translate("Calculadora", "Calculadora"))
        self.display_2.setText(_translate("Calculadora", "0"))
        self.btn_6.setText(_translate("Calculadora", "6"))
        self.btn_mp.setText(_translate("Calculadora", "×"))
        self.btn_div.setText(_translate("Calculadora", "÷"))
        self.btn_fp.setText(_translate("Calculadora", ")"))
        self.btn_8.setText(_translate("Calculadora", "8"))
        self.btn_1.setText(_translate("Calculadora", "1"))
        self.btn_9.setText(_translate("Calculadora", "9"))
        self.btn_4.setText(_translate("Calculadora", "4"))
        self.btn_pc.setText(_translate("Calculadora", "%"))
        self.btn_7.setText(_translate("Calculadora", "7"))
        self.btn_2.setText(_translate("Calculadora", "2"))
        self.btn_5.setText(_translate("Calculadora", "5"))
        self.btn_ap.setText(_translate("Calculadora", "("))
        self.btn_3.setText(_translate("Calculadora", "3"))
        self.btn_menos.setText(_translate("Calculadora", "−"))
        self.btn_ac.setText(_translate("Calculadora", "AC"))
        self.btn_0.setText(_translate("Calculadora", "0"))
        self.btn_ponto.setText(_translate("Calculadora", "."))
        self.btn_igual.setText(_translate("Calculadora", "="))
        self.btn_mais.setText(_translate("Calculadora", "+"))
        self.label.setText(_translate("Calculadora", "Programador: Iago Assunção Amorim"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculadora = QtWidgets.QMainWindow()
    ui = Ui_Calculadora()
    ui.setupUi(Calculadora)
    Calculadora.show()
    sys.exit(app.exec())