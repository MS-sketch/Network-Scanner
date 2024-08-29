# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 640)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.icon_only_widget = QtWidgets.QWidget(parent=self.page_2)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.scan_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.scan_btn_1.setMinimumSize(QtCore.QSize(38, 34))
        self.scan_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/scanner.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.scan_btn_1.setIcon(icon)
        self.scan_btn_1.setIconSize(QtCore.QSize(26, 26))
        self.scan_btn_1.setCheckable(True)
        self.scan_btn_1.setAutoExclusive(True)
        self.scan_btn_1.setObjectName("scan_btn_1")
        self.verticalLayout.addWidget(self.scan_btn_1)
        self.ai_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.ai_btn_1.setMinimumSize(QtCore.QSize(38, 34))
        self.ai_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/ai.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ai_btn_1.setIcon(icon1)
        self.ai_btn_1.setIconSize(QtCore.QSize(26, 26))
        self.ai_btn_1.setCheckable(True)
        self.ai_btn_1.setAutoExclusive(True)
        self.ai_btn_1.setObjectName("ai_btn_1")
        self.verticalLayout.addWidget(self.ai_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.settings_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.settings_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/settings.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settings_btn_1.setIcon(icon2)
        self.settings_btn_1.setIconSize(QtCore.QSize(26, 26))
        self.settings_btn_1.setObjectName("settings_btn_1")
        self.verticalLayout_3.addWidget(self.settings_btn_1)
        self.horizontalLayout_5.addWidget(self.icon_only_widget)
        self.full_menu_widget = QtWidgets.QWidget(parent=self.page_2)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_3 = QtWidgets.QLabel(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scan_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.scan_btn_2.setFont(font)
        self.scan_btn_2.setIcon(icon)
        self.scan_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.scan_btn_2.setCheckable(True)
        self.scan_btn_2.setAutoExclusive(True)
        self.scan_btn_2.setObjectName("scan_btn_2")
        self.verticalLayout_2.addWidget(self.scan_btn_2)
        self.ai_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.ai_btn_2.setFont(font)
        self.ai_btn_2.setIcon(icon1)
        self.ai_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.ai_btn_2.setCheckable(True)
        self.ai_btn_2.setAutoExclusive(True)
        self.ai_btn_2.setObjectName("ai_btn_2")
        self.verticalLayout_2.addWidget(self.ai_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.settings_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.settings_btn_2.setFont(font)
        self.settings_btn_2.setIcon(icon2)
        self.settings_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.settings_btn_2.setObjectName("settings_btn_2")
        self.verticalLayout_4.addWidget(self.settings_btn_2)
        self.horizontalLayout_5.addWidget(self.full_menu_widget)
        self.widget_3 = QtWidgets.QWidget(parent=self.page_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(parent=self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(parent=self.widget)
        self.change_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/menu-4-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.change_btn.setIcon(icon3)
        self.change_btn.setIconSize(QtCore.QSize(14, 14))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem4 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.greeting_label = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greeting_label.sizePolicy().hasHeightForWidth())
        self.greeting_label.setSizePolicy(sizePolicy)
        self.greeting_label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        self.greeting_label.setFont(font)
        self.greeting_label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.greeting_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.greeting_label.setObjectName("greeting_label")
        self.horizontalLayout_4.addWidget(self.greeting_label)
        spacerItem5 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.user__btn = QtWidgets.QPushButton(parent=self.widget)
        self.user__btn.setStyleSheet("background-color: transparent;")
        self.user__btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/account.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.user__btn.setIcon(icon4)
        self.user__btn.setIconSize(QtCore.QSize(32, 32))
        self.user__btn.setObjectName("user__btn")
        self.horizontalLayout_4.addWidget(self.user__btn)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.widget_3)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(parent=self.page_9)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.website_address_inputbox = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.website_address_inputbox.setFont(font)
        self.website_address_inputbox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.website_address_inputbox.setInputMask("")
        self.website_address_inputbox.setText("")
        self.website_address_inputbox.setObjectName("website_address_inputbox")
        self.horizontalLayout_6.addWidget(self.website_address_inputbox)
        self.clearWebAddress_btn = QtWidgets.QPushButton(parent=self.frame)
        self.clearWebAddress_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.clearWebAddress_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        self.clearWebAddress_btn.setFont(font)
        self.clearWebAddress_btn.setStyleSheet("QPushButton#clearWebAddress_btn {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(33, 150, 243, 219), stop:1 rgba(156, 39, 176, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#clearWebAddress_btn:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(63, 81, 181, 219), stop:1 rgba(103, 58, 183, 226));\n"
"}\n"
"\n"
"QPushButton#clearWebAddress_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(103, 58, 183, 255);\n"
"}\n"
"")
        self.clearWebAddress_btn.setObjectName("clearWebAddress_btn")
        self.horizontalLayout_6.addWidget(self.clearWebAddress_btn)
        self.startScan_btn = QtWidgets.QPushButton(parent=self.frame)
        self.startScan_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.startScan_btn.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setBold(True)
        self.startScan_btn.setFont(font)
        self.startScan_btn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.startScan_btn.setStyleSheet("QPushButton#startScan_btn {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(33, 150, 243, 219), stop:1 rgba(156, 39, 176, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#startScan_btn:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(63, 81, 181, 219), stop:1 rgba(103, 58, 183, 226));\n"
"}\n"
"\n"
"QPushButton#startScan_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(103, 58, 183, 255);\n"
"}\n"
"")
        self.startScan_btn.setObjectName("startScan_btn")
        self.horizontalLayout_6.addWidget(self.startScan_btn)
        self.verticalLayout_6.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.page_9)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget_4 = QtWidgets.QStackedWidget(parent=self.frame_2)
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(parent=self.page_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.outputScanResult_textedit = QtWidgets.QTextEdit(parent=self.page_3)
        self.outputScanResult_textedit.setObjectName("outputScanResult_textedit")
        self.verticalLayout_8.addWidget(self.outputScanResult_textedit)
        self.frame_8 = QtWidgets.QFrame(parent=self.page_3)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.report_generate_btn = QtWidgets.QPushButton(parent=self.frame_8)
        self.report_generate_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.report_generate_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.report_generate_btn.setFont(font)
        self.report_generate_btn.setStyleSheet("QPushButton#report_generate_btn {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(33, 150, 243, 219), stop:1 rgba(156, 39, 176, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#report_generate_btn:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(63, 81, 181, 219), stop:1 rgba(103, 58, 183, 226));\n"
"}\n"
"\n"
"QPushButton#report_generate_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(103, 58, 183, 255);\n"
"}\n"
"")
        self.report_generate_btn.setObjectName("report_generate_btn")
        self.horizontalLayout_9.addWidget(self.report_generate_btn)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.stackedWidget_4.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_5 = QtWidgets.QLabel(parent=self.page_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.stackedWidget_4.addWidget(self.page_4)
        self.verticalLayout_7.addWidget(self.stackedWidget_4)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_6 = QtWidgets.QFrame(parent=self.page_5)
        self.frame_6.setStyleSheet("background-color: #343541;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.output_window = QtWidgets.QListWidget(parent=self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.output_window.setFont(font)
        self.output_window.setStyleSheet("QListWidget {\n"
"    color: white;\n"
"}")
        self.output_window.setWordWrap(True)
        self.output_window.setObjectName("output_window")
        self.verticalLayout_16.addWidget(self.output_window)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_7.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_7.setStyleSheet("background-color: #343541;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.MessageInput_2 = QtWidgets.QLineEdit(parent=self.frame_7)
        self.MessageInput_2.setStyleSheet("    QLineEdit {\n"
"        border: 2px solid #565869;\n"
"        border-radius: 10px;\n"
"        padding: 12px;\n"
"        font-size: 16px;\n"
"        background-color: #3B3B3B;\n"
"        color: #FFFFFF;\n"
"    }\n"
"\n"
"    QLineEdit::placeholder {\n"
"        color: #9CA3AF;\n"
"    }\n"
"\n"
"")
        self.MessageInput_2.setObjectName("MessageInput_2")
        self.horizontalLayout_8.addWidget(self.MessageInput_2)
        self.SendButton_2 = QtWidgets.QPushButton(parent=self.frame_7)
        self.SendButton_2.setStyleSheet("    QPushButton {\n"
"        background-color: #10A37F;\n"
"        color: #FFFFFF;\n"
"        border-radius: 10px;\n"
"        padding: 10px;\n"
"        font-size: 16px;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #13C59D;\n"
"    }\n"
"\n"
"    QPushButton#SendButton {\n"
"        background-color: #19B797;\n"
"    }\n"
"\n"
"    QPushButton#SendButton:hover {\n"
"        background-color: #13C59D;\n"
"    }")
        self.SendButton_2.setObjectName("SendButton_2")
        self.horizontalLayout_8.addWidget(self.SendButton_2)
        self.verticalLayout_16.addWidget(self.frame_7)
        self.verticalLayout_15.addWidget(self.frame_6)
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_3 = QtWidgets.QFrame(parent=self.page_6)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(parent=self.page_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.nmap_rad = QtWidgets.QRadioButton(parent=self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.nmap_rad.setFont(font)
        self.nmap_rad.setObjectName("nmap_rad")
        self.verticalLayout_12.addWidget(self.nmap_rad)
        self.nikto_rad = QtWidgets.QRadioButton(parent=self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.nikto_rad.setFont(font)
        self.nikto_rad.setObjectName("nikto_rad")
        self.verticalLayout_12.addWidget(self.nikto_rad)
        self.header_scan_rad = QtWidgets.QRadioButton(parent=self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.header_scan_rad.setFont(font)
        self.header_scan_rad.setChecked(True)
        self.header_scan_rad.setObjectName("header_scan_rad")
        self.verticalLayout_12.addWidget(self.header_scan_rad)
        self.ok_btn = QtWidgets.QPushButton(parent=self.frame_5)
        self.ok_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.ok_btn.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet("QPushButton#ok_btn {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(33, 150, 243, 219), stop:1 rgba(156, 39, 176, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#ok_btn:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(63, 81, 181, 219), stop:1 rgba(103, 58, 183, 226));\n"
"}\n"
"\n"
"QPushButton#ok_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(103, 58, 183, 255);\n"
"}\n"
"\n"
"")
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout_12.addWidget(self.ok_btn)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem6)
        self.verticalLayout_9.addWidget(self.frame_5)
        self.stackedWidget_2.addWidget(self.page_6)
        self.verticalLayout_5.addWidget(self.stackedWidget_2)
        self.horizontalLayout_5.addWidget(self.widget_3)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.stackedWidget_3 = QtWidgets.QStackedWidget(parent=self.page)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.greeting_label_2 = QtWidgets.QLabel(parent=self.page_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greeting_label_2.sizePolicy().hasHeightForWidth())
        self.greeting_label_2.setSizePolicy(sizePolicy)
        self.greeting_label_2.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        self.greeting_label_2.setFont(font)
        self.greeting_label_2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.greeting_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.greeting_label_2.setObjectName("greeting_label_2")
        self.verticalLayout_11.addWidget(self.greeting_label_2)
        self.widget_2 = QtWidgets.QWidget(parent=self.page_10)
        self.widget_2.setMinimumSize(QtCore.QSize(561, 491))
        self.widget_2.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label_25 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_25.setGeometry(QtCore.QRect(39, 30, 231, 430))
        self.label_25.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_26.setGeometry(QtCore.QRect(270, 30, 281, 430))
        self.label_26.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_27.setGeometry(QtCore.QRect(299, 140, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_27.setObjectName("label_27")
        self.api_key = QtWidgets.QLineEdit(parent=self.widget_2)
        self.api_key.setGeometry(QtCore.QRect(300, 210, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.api_key.setFont(font)
        self.api_key.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.api_key.setObjectName("api_key")
        self.label_29 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_29.setGeometry(QtCore.QRect(40, 80, 230, 181))
        self.label_29.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_30.setGeometry(QtCore.QRect(50, 100, 180, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_30.setWordWrap(True)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_31.setGeometry(QtCore.QRect(50, 185, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.instructions_btn = QtWidgets.QPushButton(parent=self.widget_2)
        self.instructions_btn.setGeometry(QtCore.QRect(60, 360, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.instructions_btn.setFont(font)
        self.instructions_btn.setStyleSheet("QPushButton#instructions_btn {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(33, 150, 243, 219), stop:1 rgba(156, 39, 176, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#instructions_btn:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(63, 81, 181, 219), stop:1 rgba(103, 58, 183, 226));\n"
"}\n"
"\n"
"QPushButton#instructions_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(103, 58, 183, 255);\n"
"}\n"
"")
        self.instructions_btn.setObjectName("instructions_btn")
        self.label_32 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_32.setGeometry(QtCore.QRect(60, 320, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_33.setGeometry(QtCore.QRect(40, 300, 230, 121))
        self.label_33.setStyleSheet("background-color: rgba(45, 62, 80, 0.5);\n"
"")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.frame_4 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_4.setGeometry(QtCore.QRect(290, 290, 231, 61))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.api_btn = QtWidgets.QPushButton(parent=self.frame_4)
        self.api_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.api_btn.setFont(font)
        self.api_btn.setStyleSheet("QPushButton#api_btn {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#api_btn:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#api_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255);\n"
"}")
        self.api_btn.setObjectName("api_btn")
        self.verticalLayout_17.addWidget(self.api_btn)
        self.label_33.raise_()
        self.label_26.raise_()
        self.label_25.raise_()
        self.label_27.raise_()
        self.api_key.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.instructions_btn.raise_()
        self.label_32.raise_()
        self.frame_4.raise_()
        self.verticalLayout_11.addWidget(self.widget_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_11.addItem(spacerItem8)
        self.stackedWidget_3.addWidget(self.page_10)
        self.horizontalLayout.addWidget(self.stackedWidget_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.stackedWidget.addWidget(self.page)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(0)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_label_3.setText(_translate("MainWindow", "Network Scanner"))
        self.scan_btn_2.setText(_translate("MainWindow", " Scan"))
        self.ai_btn_2.setText(_translate("MainWindow", " AI Chatbot"))
        self.settings_btn_2.setText(_translate("MainWindow", " Settings"))
        self.greeting_label.setText(_translate("MainWindow", "Good [Morning/Afternoon/Evening]!"))
        self.label_2.setText(_translate("MainWindow", "Website:"))
        self.website_address_inputbox.setPlaceholderText(_translate("MainWindow", "  Website or Port"))
        self.clearWebAddress_btn.setText(_translate("MainWindow", "Clear"))
        self.startScan_btn.setText(_translate("MainWindow", "Go!"))
        self.label_3.setText(_translate("MainWindow", "Summary:"))
        self.report_generate_btn.setText(_translate("MainWindow", "Generate AI Report"))
        self.label_5.setText(_translate("MainWindow", "You Haven\'t Searched For Any Vulnerabilities. \n"
"Type A Website Or Port & Click On Go To Get Started."))
        self.MessageInput_2.setPlaceholderText(_translate("MainWindow", "Type a message..."))
        self.SendButton_2.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Please Configure Your Scan Options"))
        self.label_4.setText(_translate("MainWindow", "Select the type of scan you want."))
        self.nmap_rad.setText(_translate("MainWindow", "Nmap"))
        self.nikto_rad.setText(_translate("MainWindow", "Nikto"))
        self.header_scan_rad.setText(_translate("MainWindow", "Header Scan"))
        self.ok_btn.setText(_translate("MainWindow", "OK"))
        self.greeting_label_2.setText(_translate("MainWindow", "Good [Morning/Afternoon/Evening]!"))
        self.label_27.setText(_translate("MainWindow", "Your API Key"))
        self.api_key.setPlaceholderText(_translate("MainWindow", "  API Key"))
        self.label_30.setText(_translate("MainWindow", "Network Manager"))
        self.label_31.setText(_translate("MainWindow", "Welcome to Network Manager. \n"
"Please Enter API Key To Continue"))
        self.instructions_btn.setText(_translate("MainWindow", "I n s t r u c t i o n s"))
        self.label_32.setText(_translate("MainWindow", "Don\'t Know How?"))
        self.api_btn.setText(_translate("MainWindow", "O K"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
