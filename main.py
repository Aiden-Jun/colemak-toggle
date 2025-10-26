import keyboard

TOGGLE_KEY = "ctrl+m"

colemak_remap = {
    "d": "s", "e": "f", "f": "t", "g": "d", "i": "u", "j": "n",
    "k": "e", "l": "i", "n": "k", "o": "y", "p": ";", "r": "p",
    "s": "r", "t": "g", "u": "l", "y": "j", ";": "o",
}
for k, v in list(colemak_remap.items()):
    colemak_remap[k.upper()] = v.upper()

is_colemak = False

def toggle_layout():
    global is_colemak
    if is_colemak:
        for key in colemak_remap:
            keyboard.unremap_key(key)
        is_colemak = False
    else:
        for src, dst in colemak_remap.items():
            keyboard.remap_key(src, dst)
        is_colemak = True

keyboard.add_hotkey(TOGGLE_KEY, toggle_layout)
keyboard.wait()