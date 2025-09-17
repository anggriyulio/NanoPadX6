# main.py

import serial
import serial.tools.list_ports
import time
import pygetwindow as gw

# Impor mapping terpusat dari mappings.py
from mappings import context_actions

# ================================================================
# === KONFIGURASI
# ================================================================
BAUD_RATE = 115200
ARDUINO_READY_MSG = "READY"

# ================================================================
# === FUNGSI UTAMA
# ================================================================

def find_arduino():
    """Memindai semua COM port dan mencari Arduino yang mengirim pesan 'READY'."""
    print("Mencari Arduino...", end='', flush=True)
    ports = serial.tools.list_ports.comports()
    for port in ports:
        try:
            ser = serial.Serial(port.device, BAUD_RATE, timeout=1)
            print(f"\n- Mengecek port {port.device}...", end='', flush=True)
            time.sleep(2) # Beri waktu Arduino untuk reset
            
            line = ser.readline().decode('utf-8').strip()
            
            if ARDUINO_READY_MSG in line:
                print(f" Arduino ditemukan di {port.device}! ✅")
                return ser 
            else:
                print(" bukan.")
                ser.close()
        except (OSError, serial.SerialException):
            print(" gagal diakses.")
            continue
    print("\nArduino tidak ditemukan. Mencoba lagi...")
    return None

def main():
    """Loop utama untuk koneksi dan pembacaan data."""
    ser = None
    while True:
        try:
            if ser is None or not ser.is_open:
                ser = find_arduino()
                if ser is None:
                    time.sleep(5) 
                    continue
            
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                if not line: continue

                print(f"Data diterima: {line}")
                parts = line.split(',')
                
                if len(parts) == 3 and parts[0] == 'BTN' and parts[2] == 'DOWN':
                    button_index = parts[1]
                    
                    active_window = gw.getActiveWindow()
                    current_context = "DEFAULT"
                    
                    if active_window:
                        title = active_window.title.lower()
                        if "visual studio code" in title:
                            current_context = "vscode"
                        # TODO: Tambahkan 'elif' untuk aplikasi lain di sini
                        # elif "photoshop" in title:
                        #     current_context = "photoshop"

                    print(f"Konteks terdeteksi: {current_context.upper()}")
                    
                    # Ambil fungsi berdasarkan konteks dan index tombol
                    action_to_run = context_actions.get(current_context, {}).get(button_index)

                    if action_to_run:
                        action_to_run()
                    else:
                        print(f"Peringatan: Aksi untuk tombol {button_index} di konteks '{current_context}' tidak ditemukan.")

        except serial.SerialException:
            print("\nKoneksi Arduino terputus! 😱 Mencari kembali...")
            if ser and ser.is_open:
                ser.close()
            ser = None
            time.sleep(3)
        except KeyboardInterrupt:
            print("\nProgram dihentikan.")
            if ser and ser.is_open:
                ser.close()
            break
        except Exception as e:
            print(f"\nTerjadi error tak terduga: {e}")
            ser = None # Reset koneksi jika ada error lain
            time.sleep(5)

if __name__ == "__main__":
    main()