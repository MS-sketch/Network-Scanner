import sys
from PyQt6.QtWidgets import *
from config_diag_ui import Ui_Dialog
import os
import configparser

class MainWindow_Config:
    def __init__(self):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)

        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            api_key = config.get('API', 'gemini_api_key')
            self.ui.lineEdit.setText(api_key)

        except:
            pass

        self.ui.pushButton.clicked.connect(self.write_ini)

    def write_ini(self):
        # Create a ConfigParser object
        apikey = self.ui.lineEdit.text()
        config = configparser.ConfigParser()

        if apikey.strip() =="":
            warning = QMessageBox()
            warning.setWindowTitle("Error")
            warning.setText("API KEY CANNOT BE BLANK!")

            warning.setStandardButtons(QMessageBox.StandardButton.Ok)
            warning.setIcon(QMessageBox.Icon.Warning)
            button = warning.exec()

            if button == QMessageBox.StandardButton.Ok:
                warning.close()

        else:
            # Add sections and settings
            config['API'] = {
                'gemini_api_key': apikey
            }
            with open(r"config.ini", 'w') as config_file_obj:
                config.write(config_file_obj)
                config.flush()
                config.close()

            self.close()

    def close(self):
        self.main_win.close()

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow_Config()
    main_win.show()
    sys.exit(app.exec())