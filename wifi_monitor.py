import subprocess
import re
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv
import os

# ============================
# Wi-Fi情報取得関数
# ============================
def get_wifi_info():
    try:
        # Wi-Fi 情報
        wifi_output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode("utf-8", errors="ignore")
        ssid = re.search(r"SSID\s+:\s(.+)", wifi_output)
        signal = re.search(r"Signal\s+:\s(.+)", wifi_output)
        bssid = re.search(r"BSSID\s+:\s(.+)", wifi_output)

        # IPアドレス情報
        ip_output = subprocess.check_output("ipconfig", shell=True).decode("utf-8", errors="ignore")
        ip_match = re.search(r"IPv4 Address[. ]*: ([\d.]+)", ip_output)

        info = {
            "SSID": ssid.group(1).strip() if ssid else "N/A",
            "Signal": signal.group(1).strip() if signal else "N/A",
            "MAC(BSSID)": bssid.group(1).strip() if bssid else "N/A",
            "IP Address": ip_match.group(1).strip() if ip_match else "N/A"
        }

        return info
    except Exception as e:
        return {"Error": str(e)}

# ============================
# ログ保存関数（CSV）
# ============================
def save_log(info):
    log_file = "wifi_log.csv"
    header = ["Timestamp", "SSID", "Signal", "MAC(BSSID)", "IP Address"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [now, info.get("SSID"), info.get("Signal"), info.get("MAC(BSSID)"), info.get("IP Address")]

    file_exists = os.path.isfile(log_file)
    with open(log_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

# ============================
# GUI更新関数
# ============================
def update_info():
    info = get_wifi_info()
    if "Error" in info:
        messagebox.showerror("エラー", info["Error"])
        return
    ssid_label.config(text=f"SSID: {info.get('SSID', 'N/A')}")
    signal_label.config(text=f"Signal: {info.get('Signal', 'N/A')}")
    mac_label.config(text=f"BSSID: {info.get('MAC(BSSID)', 'N/A')}")
    ip_label.config(text=f"IP Address: {info.get('IP Address', 'N/A')}")
    save_log(info)

# ============================
# GUI構築
# ============================
root = tk.Tk()
root.title("Wi-Fi Connection Monitor")
root.geometry("400x250")
root.configure(bg="white")

title = tk.Label(root, text="Wi-Fi Connection Monitor", font=("Arial", 16, "bold"), bg="white")
title.pack(pady=10)

ssid_label = tk.Label(root, text="SSID: ", font=("Arial", 12), bg="white")
ssid_label.pack(pady=5)

signal_label = tk.Label(root, text="Signal: ", font=("Arial", 12), bg="white")
signal_label.pack(pady=5)

mac_label = tk.Label(root, text="BSSID: ", font=("Arial", 12), bg="white")
mac_label.pack(pady=5)

ip_label = tk.Label(root, text="IP Address: ", font=("Arial", 12), bg="white")
ip_label.pack(pady=5)

refresh_button = tk.Button(root, text="更新", font=("Arial", 12), command=update_info)
refresh_button.pack(pady=15)

update_info()
root.mainloop()
