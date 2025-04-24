# Wi-Fi Monitor

Windows上でWi-Fiの接続状態（SSID、BSSID、IPアドレスなど）をリアルタイムに確認できるGUIアプリです。

---

## 📌 機能

- 現在接続中のWi-Fi SSIDの表示  
- BSSID（MACアドレス）の表示  
- IPアドレスの取得  
- 更新ボタンで最新情報の取得  

---

## 🛠 使用技術

- Python  
- tkinter（GUIライブラリ）  
- subprocess（Windowsのコマンドを利用）  

---

## 🚀 使い方

### 1. 前提条件

- Windows  
- Python 3.x がインストールされていること  
  - 👉 [公式ダウンロードページ](https://www.python.org/downloads/)  
  - インストール時に「Add Python to PATH」にチェックを忘れずに！

### 2. 実行方法

コマンドプロンプトまたはPowerShellで以下を実行：

```bash
python wifi_monitor.py
または wifi_monitor.py をダブルクリックしてください。
ウィンドウが開き、現在のWi-Fi接続情報が表示されます。

📷 スクリーンショット
以下のようなウィンドウが表示されます：
![wifi表示](https://github.com/user-attachments/assets/86af156b-2e0b-4a5d-a75c-8fa59a66967a)

❓ トラブルシューティング
ウィンドウが一瞬で閉じる場合
→ PowerShell または コマンドプロンプトを開いて、以下のように直接実行してください：

bash
python wifi_monitor.py
tkinter 関連のエラーが出る場合
→ tkinter がインストールされていない可能性があります。以下のコマンドで確認できます：

bash
python -m tkinter

表示が「N/A」のままの場合
→ Wi-Fiに接続されていない、または情報取得に失敗している可能性があります。再接続後に「更新」ボタンを押してください。

🪪 ライセンス
このプロジェクトは MIT ライセンス のもとで公開されています。
自由に改変・再利用できます。

🙋‍♂️ 作者情報
名前：u-sermei

利用目的：学習・ポートフォリオ提出用

# Wi-Fi Monitor 

This GUI application allows you to check Wi-Fi connection status (SSID, BSSID, IP address, etc.) in real time on Windows.

--- 

## 📌 Features 

- Display currently connected Wi-Fi SSID 
- Display BSSID (MAC address) 
- Get IP address 
- Get latest information with refresh button 

--- 

## 🛠 Technologies used 

- Python 
- tkinter (GUI library) 
- subprocess (using Windows commands) 

--- 

## 🚀 Usage 

### 1. Prerequisites 

- Windows 
- Python 3.x installed 
 - 👉 [official download page](https://www.python.org/downloads/) 
 - Don't forget to check “Add Python to PATH” during installation!

### 2. How to run 

Run the following in a command prompt or PowerShell: 

``bash 
python wifi_monitor.py 
or double-click wifi_monitor.py.
A window will open and display the current Wi-Fi connection information.

📷 Screenshot 
A window similar to the following will appear: 
! [wifi display](https://github.com/user-attachments/assets/86af156b-2e0b-4a5d-a75c-8fa59a66967a) 

❓ Troubleshooting 
If the window closes momentarily 
→ PowerShell or Open a command prompt and run the following directly: 

bash 
python wifi_monitor.py 
If you get tkinter related errors 
→ You may not have tkinter installed. You can check with the following command: 

bash 
python -m tkinter 

If the display remains “N/A” 
→ You may not be connected to Wi-Fi or may have failed to acquire information. Please press the “Update” button after reconnecting.

🪪 License 
This project is released under the MIT License.
You can freely modify and reuse it.

🙋‍♂️ Author Info 
Name: u-sermei 

Purpose of use: for study and portfolio submission

Translated with DeepL.com (free version)


