import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
import time

# --------------------------
# Hacker-style Animation
# --------------------------
def animate_text(label):
    text = "DARKBOSS1BD Scanning for Admin Panel..."
    idx = 0
    while True:
        label.config(text=text[:idx] + "█" + text[idx+1:])
        idx = (idx + 1) % len(text)
        time.sleep(0.2)

# --------------------------
# Admin Panel Finder Function
# --------------------------
def find_admin_panel():
    url = url_entry.get().strip()
    if not url.startswith("http"):
        url = "http://" + url

    common_paths = [
        "/admin", "/login", "/admin/login", "/admin.php", "/login.php",
        "/wp-login.php", "/administrator", "/admin123", "/control",
        "/dashboard", "/admin_area", "/panel", "/moderator", "/webadmin"
    ]

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "[+] Scanning started...\n")
    found = []

    for path in common_paths:
        full_url = url.rstrip('/') + path
        try:
            response = requests.get(full_url, timeout=3)
            if response.status_code == 200:
                found.append(full_url)
                result_text.insert(tk.END, f"[+] Found: {full_url}\n")
        except:
            pass

    if not found:
        result_text.insert(tk.END, "[-] No admin panel found.\n")
    result_text.insert(tk.END, "[+] Scan Completed.\n")

# --------------------------
# Start Scan in Thread
# --------------------------
def start_scan():
    thread = threading.Thread(target=find_admin_panel)
    thread.daemon = True
    thread.start()

# --------------------------
# GUI Setup
# --------------------------
root = tk.Tk()
root.title("Darkboss1bd Admin Panel Finder - By Cyber Hacker Ak47")
root.geometry("700x500")
root.configure(bg="black")

# Banner
banner = tk.Label(root, text="🔐 ADMIN PANEL FINDER 🔐", font=("Courier", 20, "bold"), fg="lime", bg="black")
banner.pack(pady=10)

# URL Input
url_label = tk.Label(root, text="Enter Website URL:", font=("Courier", 12), fg="white", bg="black")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50, font=("Courier", 12), bg="black", fg="lime", insertbackground="lime")
url_entry.pack(pady=5)

# Scan Button
scan_button = tk.Button(root, text="🔍 SCAN", font=("Courier", 12), bg="green", fg="black", command=start_scan)
scan_button.pack(pady=10)

# Result Box
result_text = tk.Text(root, height=15, width=80, font=("Courier", 10), bg="black", fg="lime", insertbackground="lime")
result_text.pack(pady=10)

# Hacker Animation Label
anim_label = tk.Label(root, text="", font=("Courier", 12), fg="red", bg="black")
anim_label.pack(pady=5)

# Start Animation in Thread
anim_thread = threading.Thread(target=animate_text, args=(anim_label,))
anim_thread.daemon = True
anim_thread.start()

# Footer
footer = tk.Label(root, text="⚠️ For Educational Purpose Only", font=("Courier", 10), fg="yellow", bg="black")
footer.pack(side="bottom", pady=10)

# Run GUI
root.mainloop()