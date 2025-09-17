# actions/default_actions.py

import subprocess
import ctypes
import time
import pygetwindow as gw
import psutil

try:
    import pyautogui
except ImportError:
    pyautogui = None
    print("Peringatan: Library pyautogui tidak ditemukan. Aksi keyboard tidak akan berfungsi.")

def is_process_running(process_name):
    """Mengecek apakah ada proses dengan nama tertentu yang sedang berjalan."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == process_name.lower():
            return True
    return False

def action_btn_1():
    print("Aksi 1: Cek & Buka Chrome...")
    process_name = "chrome.exe"
    window_title = "Google Chrome"

    if is_process_running(process_name):
        print(f"'{process_name}' terdeteksi. Mencari jendela...")
        try:
            chrome_windows = gw.getWindowsWithTitle(window_title)
            
            if chrome_windows:
                chrome_window = chrome_windows[0]
                if chrome_window.isMinimized:
                    chrome_window.restore()
                chrome_window.activate()
                time.sleep(0.5)
                
                print("Jendela aktif, membuka tab baru (Ctrl+T).")
                if pyautogui:
                    pyautogui.hotkey('ctrl', 't')
            else:
                print("Proses Chrome ada tapi jendela tidak ditemukan. Membuka window baru.")
                subprocess.Popen(['start', 'chrome'], shell=True)
        except Exception as e:
            print(f"Terjadi error saat mengelola jendela: {e}. Membuka window baru.")
            subprocess.Popen(['start', 'chrome'], shell=True)
    else:
        print(f"'{process_name}' tidak terdeteksi, membuka window baru.")
        subprocess.Popen(['start', 'chrome'], shell=True)
        
def action_btn_2():
    print("Aksi 2: Membuka WhatsApp...")
    subprocess.Popen(['start', 'whatsapp:'], shell=True)

def action_btn_3():
    print("Aksi 3: Membuka Notepad...")
    subprocess.Popen(['notepad.exe'])

def action_btn_4():
    print("Aksi 4: Membuka Explorer...")
    subprocess.Popen(['explorer.exe'])

def action_btn_5():
    print("Aksi 5: Mute/Unmute Volume...")
    if pyautogui:
        pyautogui.press('volumemute')
    else:
        print("Gagal: pyautogui tidak terinstal.")

def action_btn_6():
    print("Aksi 6: Menampilkan Desktop...")
    if pyautogui:
        pyautogui.hotkey('win', 'd')
    else:
        print("Gagal: pyautogui tidak terinstal.")