# 🛡️ Mini IDS (Intrusion Detection System) using Scapy

A lightweight Intrusion Detection System (IDS) built with Python and Scapy for real-time network traffic monitoring, protocol analysis, alert generation, and packet logging.

## 🚀 Features

* Real-time packet sniffing
* Detects TCP, UDP, ICMP, and IGMP protocols
* Captures source and destination IP addresses
* Monitors source and destination ports
* Generates alerts for:

  * HTTP Traffic (Port 80)
  * HTTPS Traffic (Port 443)
* Logs network activity to a file
* Lightweight and beginner-friendly

---

## 📋 Requirements

* Python 3.x
* Scapy

Install Scapy:

```bash
pip install scapy
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/mini-ids.git
cd mini-ids
```

Install dependencies:

```bash
pip install scapy
```

---

## ▶️ Usage

Run the script with administrator/root privileges:

### Linux

```bash
sudo python3 ids.py
```

### Windows

Run Command Prompt as Administrator:

```bash
python ids.py
```

---

## 🔍 How It Works

1. Captures live network packets using Scapy.
2. Checks if the packet contains an IP layer.
3. Identifies the protocol type.
4. Extracts source and destination IP addresses.
5. Analyzes TCP, UDP, and ICMP traffic.
6. Detects traffic on predefined suspicious ports.
7. Generates alerts for HTTP and HTTPS traffic.
8. Logs packet information to a text file.

---

## 📂 Sample Output

```text
[ALERT] Suspicious Port Detected

Source IP: 192.168.1.10
Destination IP: 142.250.193.78
Protocol: TCP

[ALERT] HTTPS Traffic Detected
```

---

## 📝 Log File

Packet details are stored in:

```text
packet_analysis.txt
```

Example:

```text
Source IP: 192.168.1.10
Destination IP: 142.250.193.78
Protocol: TCP
Source Port: 50432
Destination Port: 443
[ALERT] Suspicious Port Detected
[ALERT] HTTPS Traffic Detected
```

---

## 🎯 Learning Objectives

This project demonstrates:

* Packet sniffing
* Network traffic analysis
* Protocol identification
* Basic IDS concepts
* Security monitoring
* Alert generation
* Log management

---

## 🔮 Future Enhancements

* Port scan detection
* Brute-force attack detection
* Blacklist and whitelist support
* Email notifications
* GUI dashboard
* SIEM integration
* CSV/JSON log export
* Threat intelligence feeds

---

## ⚠️ Disclaimer

This project is intended for educational and ethical cybersecurity purposes only. Use it only on networks that you own or have permission to monitor.

---

## 👨‍💻 Author

**Vignesh S**

Aspiring SOC Analyst | Cybersecurity Enthusiast

* LinkedIn: https://www.linkedin.com/in/vignesh-s-bbaba6397
* GitHub: https://github.com/your-username
