# Python Scheduled Port Scanner

A lightweight, scheduled port scanner built in Python using the `nmap` tool. This script automates periodic scanning of a specified IP address, logs the results, and displays them in the terminal—ideal for network administrators, penetration testers, or students learning cybersecurity fundamentals.

---

## Project Objectives

- Automatically scan a given IP address for open ports on a regular interval.
- Display the scan results in the terminal for real-time visibility.
- Log results to a file for historical reference or auditing.
- Use `nmap`, a powerful and widely-used network scanning tool.

---

##  Features

-  Customizable target IP, port range, and scan interval.
-  Real-time display of scan output.
-  Persistent logging to `nmap_scan_log.txt`.
-  Runs continuously using a scheduler loop.
-  Stealth scanning (`-sS`) for more discreet probing.

---

## Setup & Installation

### 1.  Prerequisites

- Python 3.6+
- [Nmap](https://nmap.org/download.html) installed and available in your system's PATH.

pip install python-nmap schedule

nmap --version

## Configure the script
TARGET = "192.168.1.44"         # IP address or hostname to scan
PORT_RANGE = "1-1024"           # Port range to scan
SCAN_INTERVAL = 1               # Scan frequency in minutes
LOG_FILE = "nmap_scan_log.txt"  # Output file for scan logs

Run the scanner
python scheduled_port_scanner.py

Disclaimer
This tool is intended for educational and authorized security testing purposes only. Scanning networks without permission is illegal and unethical.
