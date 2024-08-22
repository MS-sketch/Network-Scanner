import requests
import google.generativeai as palm
import translation_module as translate
import os
import subprocess
import nmap

def check_security_headers(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3"
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
                    results.append(
                        f"Warning: {header} header is present but not configured correctly. Expected: '{expected_value}', Found: '{actual_value}'")

        if missing_headers:
            results.append(f"Missing security headers: {', '.join(missing_headers)}")
        else:
            results.append("All expected security headers are present and configured correctly.")

        return "\n".join(results)

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def produce_summary(outputData, api_key):

    # Set up the PaLM API key
    palm.configure(api_key=api_key)

    model = palm.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(outputData + "\n Give a summary of these details & also provide some general fixes")

    html_formatted_text = translate.convert_text_to_html(response.text)

    return html_formatted_text

def get_cwd():
    current_directory = os.getcwd()
    return current_directory

def run_nikto_scan(url):
    cwd = get_cwd()
    # Path to the nikto.pl file (adjust this to the correct path)
    nikto_path = cwd+"\\Lib\\nikto\\program\\nikto.pl"

    print("Started Nikto Scan")

    # PowerShell command to run Nikto scan
    ps_command = f'powershell -NoProfile -ExecutionPolicy Bypass -Command "& \'{nikto_path}\' -host {url}"'

    # Run the command without showing a console window
    process = subprocess.Popen(
        ps_command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

    # Get the output and error
    output, error = process.communicate()

    # Decode the output and error
    output = output.decode('utf-8', errors='ignore')
    error = error.decode('utf-8', errors='ignore')

    total_output = "Nikto Scan Output:" + output + "\n" + "Nikto Scan Errors:" + error

    return total_output


def run_nmap_scan(url):
    # Initialize the Nmap port scanner
    nm = nmap.PortScanner()

    # Define the target IP address or hostname
    target = url

    # Define the scan options (e.g., ports 22-443)
    scan_options = '-p 22-443'

    # Run the scan
    nm.scan(target, arguments=scan_options)

    # Initialize a variable to store the scan results
    scan_results = ""

    # Store the results in the variable
    for host in nm.all_hosts():
        scan_results += f'Host : {host} ({nm[host].hostname()})\n'
        scan_results += f'State : {nm[host].state()}\n'
        for proto in nm[host].all_protocols():
            scan_results += '----------\n'
            scan_results += f'Protocol : {proto}\n'

            lport = nm[host][proto].keys()
            for port in sorted(lport):
                scan_results += f'port : {port}\tstate : {nm[host][proto][port]["state"]}\n'

    # Return the entire scan results as a single string
    return scan_results