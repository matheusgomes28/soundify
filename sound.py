from unicodedata import name
import sounddevice as sd
import numpy as np
from collections import namedtuple

def play_pure(duration, freq_hz, sps):
    Xs = np.arange(duration * sps)
    Ys = np.sin(2 * np.pi * Xs * freq_hz / sps)
    volume = 0.5
    waveform_quiet = Ys * volume

    sd.play(waveform_quiet, sps)
    sd.wait()

def play_square(duration, freq_hz, sps):

    number_samples = sps / freq_hz
    half_samples = int(number_samples / 2)
    wave = np.hstack([np.ones(half_samples), -np.ones(half_samples)])
    waveform_quiet = 0.5 * np.tile(wave, int(freq_hz * duration))

    sd.play(waveform_quiet, sps)
    sd.wait()

def play_sawtooth(duration, freq, sps):
    samples_per_curve = sps / freq
    wave = np.linspace(-1, 1, int(samples_per_curve))
    waveform_quiet = 0.5 * np.tile(wave, int(freq * duration))
    
    sd.play(waveform_quiet, sps)
    sd.wait()

def play_triangle(duration, freq, sps):
    samples_per_curve = sps / freq
    half_samples_per_curve = int(samples_per_curve / 2)
    wave = np.hstack([np.linspace(-1, 1, half_samples_per_curve), np.linspace(1, -1, half_samples_per_curve)])
    waveform_quiet = 0.5 * np.tile(wave, int(freq * duration))
    
    sd.play(waveform_quiet, sps)
    sd.wait()

def play_array(waveform, sps):
    
    sd.play(waveform, sps)
    sd.wait()

# Notes
A = 440.00
C = 523.25
E = 659.25

NotePress = namedtuple("NotePress", ("note","duration"))

song = [NotePress(A, 0.3),
NotePress(C, 0.3),
NotePress(E, 0.3),
NotePress(A, 0.3),
NotePress(C, 0.3),
NotePress(E, 0.3),
NotePress(A, 0.3),
NotePress(C, 0.3),
NotePress(E, 0.3)]



if __name__ == "__main__":

    # Samples per second
    sps = 44100

    for note, dur in song:
        play_pure(dur, note, sps)
    for note, dur in song:
        play_sawtooth(dur, note, sps)
    for note, dur in song:
        play_triangle(dur, note, sps)

    sd.stop()
    