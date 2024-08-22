import sys
from datetime import datetime

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import configparser

import network_scanner as ns
from main_win_ui import Ui_MainWindow
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
        output = None

        scan_type = self.get_scan_type()

        if scan_type == 'nmap':
            pass
        elif scan_type == 'header_scan':
            output = ns.check_security_headers(self.web_address)
        elif scan_type == 'nikto':
            pass

        response = ns.produce_summary(output)

        if response.strip() == "":
            self.scan_completed.emit("An Error Occurred!.")
        else:
            self.scan_completed.emit(response)

    def get_scan_type(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        scan = config.get('SCAN', 'scan_type')
        return scan

# Main Window Class
class MainWindow:
    def __init__(self):
        # Initialize main window with UI file
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Define important global variables
        self.web_address = None
        self.scan_type = ""
        self.api = ""

        # Progress Bar (WEBSITE)
        self.progress_bar = RotatingCircleProgressBar(self.ui.stackedWidget_4)
        self.progress_bar.setGeometry(720, 0, 50, 50)  # Adjust size and position as needed
        self.progress_bar.hide()

        # Config
        self.ui.outputScanResult_textedit.setReadOnly(True)
        self.time()
        self.ui.website_address_inputbox.textChanged.connect(self.check_integrity)
        self.disable_btn(True)
        self.ui.SendButton_2.setDisabled(True)
        self.ui.MessageInput_2.textChanged.connect(self.check_prompt_integrity)
        self.ui.api_key.textChanged.connect(self.check_api_integrety)

        # Website Summary
        self.ui.stackedWidget_4.setCurrentIndex(1)

        # Connect slots to buttons
        self.ui.startScan_btn.clicked.connect(self.start_scan)
        self.ui.clearWebAddress_btn.clicked.connect(self.clear_webAddress)

        self.ui.api_btn.clicked.connect(self.openConfigWin)

        self.ui.ok_btn.clicked.connect(self.scan_option)

        # FIX
        """self.ui.pushButton.clicked.connect(self.open_chatbot)
        self.ui.sendButton.clicked.connect(self.start_chatbot_thread)"""
        self.ui.api_btn.clicked.connect(self.write_ini)

        # MENU ITEMS
        # 1. SCAN
        self.ui.scan_btn_2.clicked.connect(self.open_scan)
        self.ui.scan_btn_1.clicked.connect(self.open_scan)

        # 2. AI
        self.ui.ai_btn_1.clicked.connect(self.open_chatbot)
        self.ui.ai_btn_2.clicked.connect(self.open_chatbot)

        # 3. SETTINGS
        self.ui.settings_btn_1.clicked.connect(self.open_settings)
        self.ui.settings_btn_2.clicked.connect(self.open_settings)

        # 4. USER
        self.ui.user__btn.clicked.connect(self.openConfigWin)

        # Rename Elements
        self.main_win.setWindowTitle("Network Scanner")

        # Edge Cases
        self.allotAPI()
        self.set_icons()

        self.ui.icon_only_widget.hide()
        self.ui.scan_btn_2.setChecked(True)

        self.read_config()

    # SCAN RELATED
    def open_scan(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def scan_type_notPresent(self):
        if self.scan_type == "" or self.scan_type == "":
            self.ui.stackedWidget_2.setCurrentIndex(2)

    def scan_option(self):

        if self.ui.nmap_rad.isChecked():
            self.scan_type = 'nmap'

        elif self.ui.header_scan_rad.isChecked():
            self.scan_type = 'header_scan'

        elif self.ui.nikto_rad.isChecked():
            self.scan_type = 'nikto'

        self.write_config()

    def start_scan(self):
        # Start the scan process with the given web address

        self.scan_type_notPresent()

        self.web_address = self.ui.website_address_inputbox.text()
        self.disable_btn(True)
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
        self.ui.outputScanResult_textedit.setHtml(response)
        self.ui.stackedWidget_4.setCurrentIndex(0)

    # SCAN TYPE
    def open_settings(self):
        self.ui.stackedWidget_2.setCurrentIndex(2)

    # API RELATED (FINISHED, NT)

    def openConfigWin(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def allotAPI(self):
        # Check For API Key
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            api_key = config.get('API', 'gemini_api_key')

            if api_key.strip() == "":
                self.openConfigWin()

            else:
                self.ui.api_key.setText(api_key)

        except:
            self.openConfigWin()

    def check_api_integrety(self):
        apikey = self.ui.api_key.text()
        if apikey.strip() == "":
            self.ui.api_btn.setDisabled(True)

        else:
            self.ui.api_btn.setEnabled(True)

    def write_ini(self):
        # Create a ConfigParser object
        self.api = self.ui.api_key.text()

        # Add sections and settings

        self.write_config()

        self.ui.stackedWidget.setCurrentIndex(0)

    # AI CHATBOT RELATED

    def open_chatbot(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)

    def check_prompt_integrity(self):
        prompt = self.ui.MessageInput_2.text()

        if prompt.strip() != "":
            self.ui.SendButton_2.setEnabled(True)

        if prompt.strip() == "":
            self.ui.SendButton_2.setDisabled(True)

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

    """def on_prompt_complete(self, prompt, output):
        # Display the AI's response in the chat display
        self.ui.sendButton.show()
        self.progress_bar2.hide()
        self.ui.chatDisplay.addItem(f"AI: \n{output}")"""



    # GENERAL ITEMS

    # CONFIG FILE
    def write_config(self):
        config = configparser.ConfigParser()

        # Read existing config to preserve other sections/keys
        config.read('config.ini')

        if not config.has_section('API'):
            config.add_section('API')

        config['API']['gemini_api_key'] = self.api
        config['API']['scan_type'] = self.scan_type

        with open('config.ini', 'w') as configfile:  # Use 'w' to overwrite
            config.write(configfile)

    def read_config(self):
        config = configparser.ConfigParser()

        config.read('config.ini')

        # Preserve existing values
        self.api = config.get('API', 'gemini_api_key', fallback="")
        self.scan_type = config.get('API', 'scan_type', fallback="header_scan")

        self.ui.api_key.setText(self.api)

        if self.api.strip() == "":
            self.ui.api_btn.setDisabled(True)

        if self.api.strip() != "":
            self.ui.api_btn.setEnabled(True)

    # ALLOTING ALL ICONS

    def set_icons(self):
        # APP LOGO
        self.main_win.setWindowIcon(QIcon("resources/icons/app_logo.png"))
        # SCAN
        self.ui.scan_btn_1.setIcon(QIcon("resources/icons/scanner_2.ico"))
        self.ui.scan_btn_2.setIcon(QIcon("resources/icons/scanner_2.ico"))
        # AI
        self.ui.ai_btn_1.setIcon(QIcon("resources/icons/ai_2.ico"))
        self.ui.ai_btn_2.setIcon(QIcon("resources/icons/ai_2.ico"))
        # SETTING
        self.ui.settings_btn_1.setIcon(QIcon("resources/icons/settings_2.ico"))
        self.ui.settings_btn_2.setIcon(QIcon("resources/icons/settings_2.ico"))
        # USER ACCOUNT
        self.ui.user__btn.setIcon(QIcon("resources/icons/account.ico"))
        # Menu
        self.ui.change_btn.setIcon(QIcon("resources/icons/menu.ico"))

    # GREET TEXT (COMPLETE, NT)
    def time(self):
        now = datetime.now()
        integer_date = int(now.strftime("%H%M%S"))

        if integer_date < 120000:
            self.setGreetText("Good Morning!")
        elif 120000 <= integer_date < 160000:
            self.setGreetText("Good Afternoon!")
        else:
            self.setGreetText("Good Evening!")

    def setGreetText(self, text):
        self.ui.greeting_label.setText(text)
        self.ui.greeting_label_2.setText(text)

    # INTEGRETY FOR WEB ADDR (COMPLETE, NT)
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


# RUN APP
if __name__ == "__main__":
    app = QApplication(sys.argv)

    style_file = QFile("resources/style.qss")
    if style_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
        style_stream = QTextStream(style_file)
        app.setStyleSheet(style_stream.readAll())
        style_file.close()

    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
