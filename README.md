# Wi-Fi Monitor

This GUI application allows you to check Wi-Fi connection status (SSID, BSSID, IP address, etc.) in real time on Windows.

---

## 📌 Functions

- Display of currently connected Wi-Fi SSID  
- Display of BSSID (MAC address)  
- Obtain IP address  
- Update button to get the latest information  

---

## 🛠 Technology used

- Python  
- tkinter (GUI library)  
- subprocess (using Windows commands)  

--- ## 🚀 Usage

## 🚀 Usage

### 1. prerequisites

- Windows  
- Python 3.x must be installed  
  - 👉 [Official download page](https://www.python.org/downloads/)  
  - Don't forget to check “Add Python to PATH” during installation!

### 2. How to run

Run the following at a command prompt or in PowerShell:

```bash
python wifi_monitor.py
Or double-click on wifi_monitor.py.
A window will open, displaying your current Wi-Fi connection information.

📷 Screenshot
A window will appear similar to the following:
! [wifi display](https://github.com/user-attachments/assets/86af156b-2e0b-4a5d-a75c-8fa59a66967a)

❓ Troubleshooting
If the window closes momentarily
→ Open PowerShell or Command Prompt and execute directly as follows

bash
python wifi_monitor.py
If you get a tkinter related error
→ tkinter may not be installed. You can check with the following command: bash python wifi_monitor.py

bash
python -m tkinter

If the display is still showing “N/A
→ You may not be connected to Wi-Fi or may have failed to acquire information. Please press the “Update” button after reconnecting.

🪪 License
This project is released under the MIT License.
You can freely modify and reuse it.

🙋‍♂️ Author Info
Name: u-sermei

Intended use: For study and portfolio submission

Translated with DeepL.com (free version)
