import tkinter as tk
from tkinter import filedialog
import librosa as rosa
import numpy as np
import soundfile as sf
from scipy.signal import fftconvolve

def main():
    
    #Filedialog start
    root = tk.Tk()
    root.withdraw()

    #Terminal print texts for user input
    print("Please select your reference file:")
    reference_path = filedialog.askopenfilename()
    print("Please select your recorded audio file:")
    recorded_path = filedialog.askopenfilename()

    if reference_path and recorded_path:
        signalProcess(reference_path, recorded_path)
    else:
        print("File selection cancelled.")

def signalProcess(reference_path, recorded_path):

    #Loading reference and recorded file
    ref_signal, sr = rosa.load(reference_path, sr=None, mono=True)
    rec_signal, _ = rosa.load(recorded_path, sr=sr, mono=True)

    #Deconvolution signal processing
    impulse_response = fftconvolve(rec_signal, ref_signal[::-1], mode='full')
    impulse_response /= np.abs(impulse_response).max()
    impulse_response = impulse_response[len(ref_signal):]

    #File saveas dialog
    file_path = filedialog.asksaveasfilename()

    print("Your IR is ready at: " + file_path)
    sf.write(file_path + ".wav", impulse_response, sr)

if __name__ == "__main__":
    main()