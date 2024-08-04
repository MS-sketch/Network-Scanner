import sys
from datetime import datetime

from PyQt6.QtCore import QThread, pyqtSignal, QTimer
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import network_scanner as ns
from main_win_ui import Ui_MainWindow


# Rotating Circle Progress Bar
class RotatingCircleProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.rotate)
        self.timer.start(50)  # Update every 50 ms

    def rotate(self):
        self.angle = (self.angle + 10) % 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rect = self.rect()
        painter.translate(rect.center())
        painter.rotate(self.angle)
        painter.translate(-rect.center())

        pen = painter.pen()
        pen.setWidth(6)
        pen.setColor(QColor(0, 0, 0))
        painter.setPen(pen)
        painter.drawArc(rect.adjusted(10, 10, -10, -10), 0 * 16, 270 * 16)


# Scan Worker Thread
class ScanWorker(QThread):
    scan_completed = pyqtSignal(str)

    def __init__(self, web_address):
        super().__init__()
        self.web_address = web_address

    def run(self):
        # Perform security headers check
        output = ns.check_security_headers(self.web_address)

        response = ns.produce_summary(output)

        if response.strip() == "":
            self.scan_completed.emit("An Error Occured!.")
        else:
            self.scan_completed.emit(response)


# Main Window Class
class MainWindow:
    def __init__(self):
        # Initialize main window with UI file
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # Define important global variables
        self.web_address = None

        # Progress Bar
        self.progress_bar = RotatingCircleProgressBar(self.ui.frame_12)
        self.progress_bar.setGeometry(120, 0, 50, 50)  # Adjust size and position as needed
        self.progress_bar.hide()

        # Config
        self.ui.outputScanResult_textedit.setReadOnly(True)
        self.time()
        self.ui.website_address_inputbox.textChanged.connect(self.check_integrity)
        self.disable_btn(True)

        # Connect slots to buttons
        self.ui.startScan_btn.clicked.connect(self.start_scan)
        self.ui.clearWebAddress_btn.clicked.connect(self.clear_webAddress)

        # Rename Elements
        self.main_win.setWindowTitle("Network Scanner")

    def start_scan(self):
        # Start the scan process with the given web address
        self.web_address = self.ui.website_address_inputbox.text()
        self.disable_btn(True)
        self.ui.configSettings_btn.setDisabled(True)
        self.ui.startScan_btn.hide()
        self.progress_bar.show()

        # Initialize and start the scan worker
        self.worker = ScanWorker(self.web_address)
        self.worker.scan_completed.connect(self.on_scan_complete)
        self.worker.start()

    def on_scan_complete(self, response):
        # Hide progress bar, re-enable buttons, and display scan result
        self.progress_bar.hide()
        self.ui.startScan_btn.show()
        self.disable_btn(False)
        self.ui.configSettings_btn.setDisabled(False)
        self.ui.outputScanResult_textedit.setHtml(response)

    def time(self):
        now = datetime.now()
        integer_date = int(now.strftime("%H%M%S"))

        if integer_date < 120000:
            self.ui.greeting_label.setText("Good Morning!")
        elif 120000 <= integer_date < 160000:
            self.ui.greeting_label.setText("Good Afternoon!")
        else:
            self.ui.greeting_label.setText("Good Evening!")

    def disable_btn(self, condition):
        # Enable or disable buttons based on the condition
        self.ui.startScan_btn.setDisabled(condition)
        self.ui.clearWebAddress_btn.setDisabled(condition)

    def check_integrity(self):
        webAddress = self.ui.website_address_inputbox.text()

        if webAddress.strip() == "":
            self.disable_btn(True)
        else:
            self.disable_btn(False)

    def clear_webAddress(self):
        self.ui.website_address_inputbox.setText("")

    def show(self):
        # Show the main window
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
