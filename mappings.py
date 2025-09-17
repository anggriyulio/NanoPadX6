# mappings.py

# Impor semua fungsi dari file-file aksi
from actions.default_actions import (
    action_btn_1, 
    action_btn_2, 
    action_btn_3, 
    action_btn_4, 
    action_btn_5, 
    action_btn_6
)
from actions.vscode_actions import (
    action_vscode_command_palette,
    action_vscode_toggle_terminal,
    action_vscode_find_file,
    action_vscode_run_debug,
    action_vscode_format_file
)

context_actions = {
    "DEFAULT": {
        '1': action_btn_1, # Buka Chrome
        '2': action_btn_2, # Buka WhatsApp
        '3': action_btn_3, # Buka Notepad
        '4': action_btn_4, # Buka Explorer
        '5': action_btn_5, # Mute/Unmute
        '6': action_btn_6, # Lock Workstation
    },
    "vscode": {
        '1': action_vscode_command_palette,
        '2': action_vscode_find_file,
        '3': action_vscode_toggle_terminal,
        '4': action_vscode_run_debug,
        '5': action_vscode_format_file,
        '6': action_btn_6, # Tombol 6 fungsinya tetap sama (global)
    }
    # TODO: Tambahkan konteks baru di sini
    # "photoshop": {
    #     '1': action_photoshop_new_layer,
    #     ...
    # }
}