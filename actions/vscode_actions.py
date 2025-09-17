# actions/vscode_actions.py

try:
    import pyautogui
except ImportError:
    pyautogui = None

def action_vscode_command_palette():
    """Membuka Command Palette di VS Code (Ctrl+Shift+P)."""
    print("Aksi VS Code: Command Palette")
    if pyautogui:
        pyautogui.hotkey('ctrl', 'shift', 'p')

def action_vscode_toggle_terminal():
    """Membuka atau menutup terminal terintegrasi di VS Code (Ctrl+`)."""
    print("Aksi VS Code: Toggle Terminal")
    if pyautogui:
        pyautogui.hotkey('ctrl', '`')

def action_vscode_find_file():
    """Membuka pencarian file (Go to File) di VS Code (Ctrl+P)."""
    print("Aksi VS Code: Find File")
    if pyautogui:
        pyautogui.hotkey('ctrl', 'p')

def action_vscode_run_debug():
    """Memulai sesi debugging di VS Code (F5)."""
    print("Aksi VS Code: Run Debug")
    if pyautogui:
        pyautogui.press('f5') 

def action_vscode_format_file():
    """Merformat dokumen yang sedang aktif di VS Code (Shift+Alt+F)."""
    print("Aksi VS Code: Format File")
    if pyautogui:
        pyautogui.hotkey('shift', 'alt', 'f')