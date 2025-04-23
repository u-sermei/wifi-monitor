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

