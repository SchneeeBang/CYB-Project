import nmap
import schedule
import time
from datetime import datetime

# ========== CONFIGURATION ==========
TARGET = "192.168.1.44"            # Replace with your target IP or hostname
PORT_RANGE = "1-1024"           # Port range to scan
SCAN_INTERVAL = 1             # In minutes
LOG_FILE = "nmap_scan_log.txt"  # Log file
# ===================================

def scan_and_display():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n[+] Starting scan on {TARGET} at {timestamp}")
    scanner = nmap.PortScanner()

    try:
        scanner.scan(hosts=TARGET, ports=PORT_RANGE, arguments='-sS')
    except Exception as e:
        print(f"[!] Scan error: {e}")
        return

    log_lines = [f"\n[{timestamp}] Scan Results for {TARGET}"]
    for host in scanner.all_hosts():
        log_lines.append(f"Host: {host} ({scanner[host].hostname()})")
        log_lines.append(f"State: {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            log_lines.append(f"Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in sorted(ports):
                state = scanner[host][proto][port]['state']
                log_lines.append(f"Port: {port}\tState: {state}")
    log_lines.append("-" * 40)

    # Write to log file
    with open(LOG_FILE, "a") as f:
        for line in log_lines:
            f.write(line + "\n")

    # Display results
    print("\n".join(log_lines))

# Schedule the scan
schedule.every(SCAN_INTERVAL).minutes.do(scan_and_display)

print(f"[*] Scheduled port scanner started. Scanning {TARGET} every {SCAN_INTERVAL} minutes.")
scan_and_display()  # Initial scan

# Loop
while True:
    schedule.run_pending()
    time.sleep(1)
