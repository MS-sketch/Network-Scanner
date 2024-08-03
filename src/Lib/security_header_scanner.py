import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel
from PyQt6.QtGui import QIcon

def check_security_headers(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        security_headers = {
            "Strict-Transport-Security": "max-age",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "X-Content-Type-Options": "nosniff",
            "Content-Security-Policy": "default-src",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Permissions-Policy": "geolocation=(), microphone=()",
            "Feature-Policy": "geolocation 'none'; microphone 'none';",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Expose-Headers": "Content-Length, Content-Range",
            "Content-Security-Policy-Report-Only": "default-src 'self'",
            "Cross-Origin-Embedder-Policy": "require-corp",
            "Cross-Origin-Opener-Policy": "same-origin",
            "Cross-Origin-Resource-Policy": "same-origin",
            "Expect-CT": "max-age=0",
            "Public-Key-Pins": "pin-sha256",
            "X-Permitted-Cross-Domain-Policies": "none",
            "X-DNS-Prefetch-Control": "on",
            "X-Download-Options": "noopen",
            "X-Content-Security-Policy": "default-src 'self'",
            "X-WebKit-CSP": "default-src 'self'"
        }

        missing_headers = []
        results = []
        for header, expected_value in security_headers.items():
            if header not in response.headers:
                missing_headers.append(header)
            else:
                actual_value = response.headers[header]
                if expected_value and expected_value not in actual_value:
                    results.append(f"Warning: {header} header is present but not configured correctly. Expected: '{expected_value}', Found: '{actual_value}'")

        if missing_headers:
            results.append(f"Missing security headers: {', '.join(missing_headers)}")
        else:
            results.append("All expected security headers are present and configured correctly.")

        return "\n".join(results)

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

class SecurityHeaderScanner(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set window title and icon
        self.setWindowTitle('Security Header Scanner')
        self.setWindowIcon(QIcon('icon.png'))

        # Create layout
        layout = QVBoxLayout()

        # Create and add widgets
        self.url_label = QLabel('Enter the URL to scan:')
        layout.addWidget(self.url_label)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('http://example.com')
        layout.addWidget(self.url_input)

        self.scan_button = QPushButton('Scan')
        self.scan_button.clicked.connect(self.on_scan)
        layout.addWidget(self.scan_button)

        self.results_area = QTextEdit()
        self.results_area.setReadOnly(True)
        layout.addWidget(self.results_area)

        # Set the layout
        self.setLayout(layout)
        self.resize(600, 400)

    def on_scan(self):
        url = self.url_input.text()
        if not url:
            self.results_area.setText("Please enter a URL.")
            return
        results = check_security_headers(url)
        self.results_area.setText(results)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SecurityHeaderScanner()
    ex.show()
    sys.exit(app.exec())