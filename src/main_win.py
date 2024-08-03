from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from main_win_ui import Ui_MainWindow
import sys
from datetime import datetime
import os
import network_scanner as ns
import summary_generator as sg
from Custom_Widgets.QCustomLoadingIndicators import QCustomSpinner


# Scan Worker Thread
class ScanWorker(QThread):
    progress_changed = pyqtSignal(int)
    scan_completed = pyqtSignal(str)

    def __init__(self, web_address):
        super().__init__()
        self.web_address = web_address

    def run(self):
        # Simulating scan process with progress updates
        output = ns.check_security_headers(self.web_address)
        response = sg.genAI(output)
        self.scan_completed.emit(response)

# MAIN WINDOW CLASS
class MainWindow:
    def __init__(self):
        # DEFINED MAIN WINDOW WITH THE PY UI FILE FROM PYUIC6
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # DEFINING IMPORTANT GLOBAL VARIABLES.
        self.web_address = None

        # PROGRESS BAR
        self.spinner = QCustomSpinner(
            lineWidth=2,
            lineColor=None,  # Use default color if None
            direction="Clockwise",  # or "Counterclockwise"
            animationType="Bounce"  # or "Smooth"
        )

        self.spinner.show()

        # CONFIG
        self.ui.outputScanResult_textedit.setReadOnly(True)
        self.time()

        # SLOTS WITH BUTTONS

        # 1. Start Scan BTN
        self.ui.startScan_btn.clicked.connect(self.start_scan)

    def start_scan(self):
        # START THE ANALYSIS WITH THE HELP OF SECURITY HEADER FRAMEWORK.
        self.web_address = self.ui.website_address_inputbox.text()
        # Disable BTN
        self.disable_btn(True)
        # INIT SCAN
        output = ns.check_security_headers(self.web_address)

        response = sg.genAI(output)
        # ENABLE BTN
        self.disable_btn(False)

        self.ui.outputScanResult_textedit.setPlainText(response)

    def time(self):
        now = datetime.now()
        integer_date = int(now.strftime("%H%M%S"))

        if integer_date < 120000:
            self.ui.greeting_label.setText("Good Morning!")

        elif 120000 > integer_date > 160000:
            self.ui.greeting_label.setText("Good Afternoon!")

        else:
            self.ui.greeting_label.setText("Good Evening!")

    def disable_btn(self, condition):
        # DISABLES BTN
        if condition:
            self.ui.startScan_btn.setDisabled(True)
            self.ui.clearWebAddress_btn.setDisabled(True)
            self.ui.configSettings_btn.setDisabled(True)

        elif not condition:
            self.ui.startScan_btn.setEnabled(True)
            self.ui.clearWebAddress_btn.setEnabled(True)
            self.ui.configSettings_btn.setEnabled(True)

    def show(self):
        # SHOW MAIN WINDOW
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
