from PyQt5 import QtCore, QtGui, QtWidgets
import options

class Ui_MainWindow(object):
    def __init__(self):
        self.opt = options.Option()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMaximumWidth(904)
        MainWindow.setMaximumHeight(675)
        MainWindow.setMinimumWidth(904)
        MainWindow.setMinimumHeight(675)
        MainWindow.resize(904, 675)
        MainWindow.setWindowIcon(QtGui.QIcon("ico.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plot = QtWidgets.QLabel(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(0, 0, 571, 461))
        self.plot.setText("")
        self.plot.setPixmap(QtGui.QPixmap("plot.png"))
        self.plot.setScaledContents(True)
        self.plot.setObjectName("plot")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(580, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.draw = QtWidgets.QPushButton(self.centralwidget)
        self.draw.setGeometry(QtCore.QRect(640, 530, 211, 101))
        self.draw.clicked.connect(self.fDraw)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.draw.setFont(font)
        self.draw.setObjectName("draw")
        self.ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ProgressBar.setGeometry(QtCore.QRect(10, 480, 561, 23))
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("ProgressBar")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 510, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(178, 512, 351, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.error.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.error.setFont(font)
        self.error.setObjectName("error")
        self.function = QtWidgets.QLineEdit(self.centralwidget)
        self.function.setGeometry(QtCore.QRect(580, 30, 301, 21))
        self.function.setObjectName("function")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(580, 60, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(580, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.leftrange = QtWidgets.QLineEdit(self.centralwidget)
        self.leftrange.setGeometry(QtCore.QRect(580, 100, 301, 20))
        self.leftrange.setInputMask("")
        self.leftrange.setObjectName("leftrange")
        self.rightrange = QtWidgets.QLineEdit(self.centralwidget)
        self.rightrange.setGeometry(QtCore.QRect(580, 170, 301, 20))
        self.rightrange.setInputMask("")
        self.rightrange.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.rightrange.setObjectName("rightrange")
        self.step = QtWidgets.QSlider(self.centralwidget)
        self.step.setGeometry(QtCore.QRect(580, 240, 301, 22))
        self.step.setMinimum(1)
        self.step.setMaximum(100)
        self.step.setProperty("value", 50)
        self.step.setOrientation(QtCore.Qt.Horizontal)
        self.step.setObjectName("step")
        self.step.valueChanged.connect(self.fStep)
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(580, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.steplabel = QtWidgets.QLabel(self.centralwidget)
        self.steplabel.setGeometry(QtCore.QRect(710, 270, 47, 13))
        self.steplabel.setObjectName("steplabel")
        self.Label6 = QtWidgets.QLabel(self.centralwidget)
        self.Label6.setGeometry(QtCore.QRect(580, 280, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Label6.setFont(font)
        self.Label6.setObjectName("Label6")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(700, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.xaxis = QtWidgets.QCheckBox(self.centralwidget)
        self.xaxis.setGeometry(QtCore.QRect(590, 320, 70, 17))
        self.xaxis.setObjectName("xaxis")
        self.yaxis = QtWidgets.QCheckBox(self.centralwidget)
        self.yaxis.setGeometry(QtCore.QRect(790, 320, 70, 17))
        self.yaxis.setObjectName("yaxis")
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(700, 340, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.min = QtWidgets.QCheckBox(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(590, 370, 80, 17))
        self.min.setObjectName("min")
        self.max = QtWidgets.QCheckBox(self.centralwidget)
        self.max.setGeometry(QtCore.QRect(680, 370, 80, 17))
        self.max.setObjectName("max")
        self.root = QtWidgets.QCheckBox(self.centralwidget)
        self.root.setGeometry(QtCore.QRect(790, 370, 70, 17))
        self.root.setObjectName("root")
        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(650, 390, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.montecarlo = QtWidgets.QCheckBox(self.centralwidget)
        self.montecarlo.setGeometry(QtCore.QRect(590, 410, 91, 17))
        self.montecarlo.setObjectName("montecarlo")
        self.label9 = QtWidgets.QLabel(self.centralwidget)
        self.label9.setGeometry(QtCore.QRect(670, 410, 47, 16))
        self.label9.setObjectName("label9")
        self.n_monte = QtWidgets.QSlider(self.centralwidget)
        self.n_monte.setGeometry(QtCore.QRect(700, 410, 201, 22))
        self.n_monte.setMinimum(10)
        self.n_monte.setMaximum(2000)
        self.n_monte.setProperty("value", 10)
        self.n_monte.setOrientation(QtCore.Qt.Horizontal)
        self.n_monte.setObjectName("n_monte")
        self.n_monte.valueChanged.connect(self.fMonte)
        self.nlabel = QtWidgets.QLabel(self.centralwidget)
        self.nlabel.setGeometry(QtCore.QRect(780, 430, 47, 13))
        self.nlabel.setObjectName("nlabel")
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setGeometry(QtCore.QRect(10, 540, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label10.setFont(font)
        self.label10.setObjectName("label10")
        self.info = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(10, 560, 341, 90))
        self.info.setReadOnly(True)
        self.info.setPlainText("")
        self.info.setObjectName("info")
        self.rectangle = QtWidgets.QCheckBox(self.centralwidget)
        self.rectangle.setGeometry(QtCore.QRect(590, 440, 111, 17))
        self.rectangle.setObjectName("rectangle")
        self.label9_2 = QtWidgets.QLabel(self.centralwidget)
        self.label9_2.setGeometry(QtCore.QRect(700, 440, 47, 16))
        self.label9_2.setObjectName("label9_2")
        self.width = QtWidgets.QSlider(self.centralwidget)
        self.width.setGeometry(QtCore.QRect(750, 440, 151, 22))
        self.width.setMinimum(1)
        self.width.setMaximum(1000)
        self.width.setProperty("value", 1)
        self.width.setOrientation(QtCore.Qt.Horizontal)
        self.width.setObjectName("width")
        self.width.valueChanged.connect(self.fRect)
        self.widthlabel = QtWidgets.QLabel(self.centralwidget)
        self.widthlabel.setGeometry(QtCore.QRect(790, 460, 47, 13))
        self.widthlabel.setObjectName("widthlabel")
        self.label11 = QtWidgets.QLabel(self.centralwidget)
        self.label11.setGeometry(QtCore.QRect(690, 470, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label11.setFont(font)
        self.label11.setObjectName("label11")
        self.vertical = QtWidgets.QCheckBox(self.centralwidget)
        self.vertical.setGeometry(QtCore.QRect(590, 490, 80, 17))
        self.vertical.setObjectName("vertical")
        self.horizontal = QtWidgets.QCheckBox(self.centralwidget)
        self.horizontal.setGeometry(QtCore.QRect(780, 490, 80, 17))
        self.horizontal.setObjectName("horizontal")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(420, 530, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.fClear)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plot"))
        self.label1.setText(_translate("MainWindow", "Function :"))
        self.draw.setText(_translate("MainWindow", "Draw"))
        self.label2.setText(_translate("MainWindow", ""))
        self.error.setText(_translate("MainWindow", ""))
        self.label3.setText(_translate("MainWindow", "Left range:"))
        self.label4.setText(_translate("MainWindow", "Right range:"))
        self.label5.setText(_translate("MainWindow", "Step:"))
        self.steplabel.setText(_translate("MainWindow", "0.5"))
        self.Label6.setText(_translate("MainWindow", "Draw--------------------------------------------"))
        self.label6.setText(_translate("MainWindow", "Axis:"))
        self.xaxis.setText(_translate("MainWindow", "X-Axis"))
        self.yaxis.setText(_translate("MainWindow", "Y-Axis"))
        self.label7.setText(_translate("MainWindow", "Find:"))
        self.min.setText(_translate("MainWindow", "Minimum"))
        self.max.setText(_translate("MainWindow", "Maximum"))
        self.root.setText(_translate("MainWindow", "Root"))
        self.label8.setText(_translate("MainWindow", "Integral methods:"))
        self.montecarlo.setText(_translate("MainWindow", "M. Carlo"))
        self.label9.setText(_translate("MainWindow", "|N = "))
        self.nlabel.setText(_translate("MainWindow", "10"))
        self.label10.setText(_translate("MainWindow", "Info:"))
        self.rectangle.setText(_translate("MainWindow", "Rec. method"))
        self.label9_2.setText(_translate("MainWindow", "|Width = "))
        self.widthlabel.setText(_translate("MainWindow", "1"))
        self.label11.setText(_translate("MainWindow", "Mirror"))
        self.vertical.setText(_translate("MainWindow", "Vertical"))
        self.horizontal.setText(_translate("MainWindow", "Horizontal"))
        self.clear.setText(_translate("MainWindow", "Clear"))

    def fMonte(self):
        """
        Monte Carlo button
        """
        self.opt.n_monte = self.n_monte.value()
        self.nlabel.setText(str(self.opt.n_monte))
        self.nlabel.adjustSize()

    def fRect(self):
        """
        Rectangle method button
        """
        self.opt.width_rect = self.width.value()
        self.widthlabel.setText(str(self.opt.width_rect))
        self.widthlabel.adjustSize()

    def fStep(self):
        """
        step slide
        """
        self.opt.step = self.step.value()/100
        self.steplabel.setText(str(self.opt.step))
        self.steplabel.adjustSize()


    def fDraw(self):
        """
        Draw plot
        """
        self.ProgressBar.setValue(0)
        try:
            self.opt.man.new_function(self.function.text())
        except:
            self.fError("Bad function")
            return

        try:
            self.opt.set_a(float(self.leftrange.text()))
        except:
            self.fError("Bad left range!")
            return

        try:
            self.opt.set_b(float(self.rightrange.text()))
        except:
            self.fError("Bad right range!")
            return

        self.opt.xline = self.xaxis.isChecked()
        self.opt.yline = self.yaxis.isChecked()
        self.opt.fmin = self.min.isChecked()
        self.opt.fmax = self.max.isChecked()
        self.opt.froot = self.root.isChecked()
        self.opt.monte = self.montecarlo.isChecked()
        self.opt.rectangle = self.rectangle.isChecked()
        self.opt.verti = self.vertical.isChecked()
        self.opt.horiz = self.horizontal.isChecked()
        try:
            data = self.opt.plot(self.ProgressBar)
        except Exception as inst:
            self.fError(str(inst))
            return
        self.fUpdate(data)
        self.ProgressBar.setValue(100)
        self.fError(None)

    def fClear(self):
        """
        Clear plot
        """
        self.ProgressBar.setValue(0)
        self.opt.clear()
        self.fUpdate()
        self.fError(None)

    def fError(self, Text):
        """
        Print error message
        """
        if Text == None:
            self.error.setText('')
            self.label2.setText('')
        else:
            self.label2.setText('Error message :')
            self.error.setText(Text)

    def fUpdate(self, data=None):
        """
        Update plot
        """
        self.plot.setPixmap(QtGui.QPixmap("plot.png"))
        if data == None:
            self.info.setPlainText("")
        else:
            text = self.info.toPlainText()
            text += '--------------------------\n'
            text += 'Function : ' + self.opt.man.function + '\n'
            text += "Minimum : " + str(data["min"]) + '\n'
            text += "Maximum : " + str(data["max"]) + '\n'
            text += "Root : " + str(data["root"]) + '\n'
            text += "Integral : " + str(data["integral"]) + '\n'
            text += "Monte Carlo integral : " + str(data["monte"]) + '\n'
            text += "Rectangle method integral : " + str(data["rect"]) + '\n'
            text += '--------------------------\n'
            self.info.setPlainText(text)
