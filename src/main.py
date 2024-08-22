import nmap

def check_nmap():
    try:
        # Initialize the Nmap port scanner
        nm = nmap.PortScanner()

        # Perform a basic scan on localhost (127.0.0.1)
        nm.scan('127.0.0.1', arguments='-p 80')

        # Check if any hosts were found
        if nm.all_hosts():
            print("Nmap is working correctly!")
            for host in nm.all_hosts():
                print(f'Host : {host} ({nm[host].hostname()})')
                print(f'State : {nm[host].state()}')
                for proto in nm[host].all_protocols():
                    print('----------')
                    print(f'Protocol : {proto}')
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        print(f'port : {port}\tstate : {nm[host][proto][port]["state"]}')
        else:
            print("Nmap is installed but no hosts were found.")

    except nmap.PortScannerError as e:
        print(f"Error: {e}")
        print("Nmap may not be installed correctly, or there might be a problem with your Nmap installation.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("There may be an issue with your Nmap installation or environment.")

# Run the check
check_nmap()
