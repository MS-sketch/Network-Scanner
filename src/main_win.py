import sys
from datetime import datetime

from PyQt6.QtCore import QThread, pyqtSignal, QTimer
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import network_scanner as ns
from main_win_ui import Ui_MainWindow
from config_diag import MainWindow_Config
import chatbot_manager as cm


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

# Create Response Worker Thread
class ChatbotWorker(QThread):
    prompt_completed = pyqtSignal(str, str)

    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt

    def run(self):
        # Generate the chatbot response
        output = cm.create_chatbot(self.prompt)
        self.prompt_completed.emit(self.prompt, output)

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

        # Define External Dialog
        self.config_window = MainWindow_Config()

        # Progress Bar
        self.progress_bar = RotatingCircleProgressBar(self.ui.frame_12)
        self.progress_bar.setGeometry(720, 0, 50, 50)  # Adjust size and position as needed
        self.progress_bar.hide()

        # Progress Bar 2
        self.progress_bar2 = RotatingCircleProgressBar(self.ui.send_frame)
        self.progress_bar2.setGeometry(0, 0, 30, 30)  # Adjust size and position as needed
        self.progress_bar2.hide()

        # Config
        self.ui.outputScanResult_textedit.setReadOnly(True)
        self.time()
        self.ui.website_address_inputbox.textChanged.connect(self.check_integrity)
        self.disable_btn(True)
        self.ui.sendButton.setDisabled(True)
        self.ui.messageInput.textChanged.connect(self.check_prompt_integrity)

        # Connect slots to buttons
        self.ui.startScan_btn.clicked.connect(self.start_scan)
        self.ui.clearWebAddress_btn.clicked.connect(self.clear_webAddress)
        self.ui.configSettings_btn.clicked.connect(self.openConfigWin)
        self.ui.pushButton.clicked.connect(self.open_chatbot)
        self.ui.back_to_home.clicked.connect(self.close_chatbot)
        self.ui.sendButton.clicked.connect(self.start_chatbot_thread)

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

    def openConfigWin(self):
        self.config_window.show()

    def check_prompt_integrity(self):
        prompt = self.ui.messageInput.text()

        if prompt.strip() != "":
            self.ui.sendButton.setEnabled(True)

        if prompt.strip() == "":
            self.ui.sendButton.setDisabled(True)

    def start_chatbot_thread(self):
        # Get the prompt text and start the chatbot worker
        prompt = self.ui.messageInput.text()
        self.ui.chatDisplay.addItem("You: \n" + prompt)

        # Initialize and start the chatbot worker
        self.ui.sendButton.hide()
        self.progress_bar2.show()

        self.chatbot_worker = ChatbotWorker(prompt)
        self.chatbot_worker.prompt_completed.connect(self.on_prompt_complete)
        self.chatbot_worker.start()

    def on_prompt_complete(self, prompt, output):
        # Display the AI's response in the chat display
        self.ui.sendButton.show()
        self.progress_bar2.hide()
        self.ui.chatDisplay.addItem(f"AI: \n{output}")

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

    def open_chatbot(self):
        self.ui.mainwindow_stackWidget.setCurrentIndex(1)

    def close_chatbot(self):
        self.ui.mainwindow_stackWidget.setCurrentIndex(0)
        self.ui.messageInput.setText("")
        self.ui.chatDisplay.clear()

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
