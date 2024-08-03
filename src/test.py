from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from main_win_ui import Ui_MainWindow
import sys
from datetime import datetime
import network_scanner as ns
import summary_generator as sg

# Worker Thread
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

# Main Window
class MainWindow:
    def __init__(self):
        # DEFINED MAIN WINDOW WITH THE PY UI FILE FROM PYUIC6
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # DEFINING IMPORTANT GLOBAL VARIABLES.
        self.web_address = None

        # CONFIG
        self.ui.outputScanResult_textedit.setReadOnly(True)
        self.time()

        # Progress Bar
        self.progress_bar = QProgressBar(self.main_win)
        self.progress_bar.setGeometry(20, 100, 280, 30)  # Set position and size
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setRange(0, 0)  # Set to an indeterminate progress

        # SLOTS WITH BUTTONS

        # 1. Start Scan BTN
        self.ui.startScan_btn.clicked.connect(self.start_scan)

    def start_scan(self):
        # START THE ANALYSIS WITH THE HELP OF SECURITY HEADER FRAMEWORK.
        self.web_address = self.ui.website_address_inputbox.text()
        # Disable BTN
        self.disable_btn(True)
        # Show Progress Bar
        self.progress_bar.show()

        # INIT SCAN
        self.worker = ScanWorker(self.web_address)
        self.worker.scan_completed.connect(self.on_scan_complete)
        self.worker.start()

    def on_scan_complete(self, response):
        # Hide Progress Bar
        self.progress_bar.hide()
        # ENABLE BTN
        self.disable_btn(False)
        # Display the scan result
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
