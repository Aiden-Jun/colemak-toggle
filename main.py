import numpy
import keyboard
import simpleaudio

TOGGLE_KEY = "ctrl+m"

colemak_remap = {
    "d": "s", "e": "f", "f": "t", "g": "d", "i": "u", "j": "n",
    "k": "e", "l": "i", "n": "k", "o": "y", "p": ";", "r": "p",
    "s": "r", "t": "g", "u": "l", "y": "j", ";": "o",
}
for k, v in list(colemak_remap.items()):
    colemak_remap[k.upper()] = v.upper()

is_colemak = False

def play_wave(frequency, duration=0.5, volume=0.5, wave_type="sine"):
    sample_rate = 44100
    t = numpy.linspace(0, duration, int(sample_rate * duration), False)
    
    if wave_type == "sine":
        wave = numpy.sin(2 * numpy.pi * frequency * t)
    elif wave_type == "square":
        wave = numpy.sign(numpy.sin(2 * numpy.pi * frequency * t))
    elif wave_type == "sawtooth":
        wave = 2 * (t * frequency - numpy.floor(t * frequency + 0.5))
    elif wave_type == "triangle":
        wave = 2 * numpy.abs(2 * (t * frequency - numpy.floor(t * frequency + 0.5))) - 1
    else:
        wave = numpy.sin(2 * numpy.pi * frequency * t)
    
    audio = (wave * (2**15 - 1) * volume).astype(numpy.int16)
    simpleaudio.play_buffer(audio, 1, 2, sample_rate).wait_done()

def noise1():
    play_wave(880, wave_type="sine")

def noise2():
    play_wave(220, wave_type="sine")

def toggle_layout():
    global is_colemak
    if is_colemak:
        for key in colemak_remap:
            keyboard.unremap_key(key)
        is_colemak = False
        noise1()
    else:
        for src, dst in colemak_remap.items():
            keyboard.remap_key(src, dst)
        is_colemak = True
        noise2()

keyboard.add_hotkey(TOGGLE_KEY, toggle_layout)
keyboard.wait()
