# CYB-Project# 🔍 Scheduled Port Scanner with Nmap (Python)

This Python script performs **automated scheduled port scans** using the `nmap` tool and logs the results to a file. It displays the scanned information in real time and runs continuously at a defined interval.

---

## 📦 Features

- Scans a target IP or hostname using `nmap`
- Configurable port range and scan interval
- Displays live scan output in the terminal
- Logs scan results to `nmap_scan_log.txt`
- Runs continuously using a scheduled loop

---

## 🛠️ Requirements

Install the required Python packages:

```bash
pip install python-nmap schedule
nmap --version
pip install schedule
