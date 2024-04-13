import tkinter as tk
from tkinter import filedialog
import librosa as rosa
import numpy as np
import soundfile as sf
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def main():
    
    # Filedialog start
    root = tk.Tk()
    root.withdraw()

    # Terminal print texts for user input
    print("Please select your reference file:")
    reference_path = filedialog.askopenfilename(title="Reference Wave File")
    print("Please select your recorded audio file:")
    recorded_path = filedialog.askopenfilename(title="Recorded Wave File")

    if reference_path and recorded_path:
        signalProcess(reference_path, recorded_path)
        plotFig()
    else:
        print("File selection cancelled.")

def signalProcess(reference_path, recorded_path):

    # Loading reference and recorded file
    global sr
    ref_signal, sr = rosa.load(reference_path, sr=None, mono=True)
    rec_signal, _ = rosa.load(recorded_path, sr=sr, mono=True)

    # Deconvolution signal processing
    global impulse_response
    impulse_response = fftconvolve(rec_signal, ref_signal[::-1], mode='full')
    impulse_response /= np.abs(impulse_response).max()
    impulse_response = impulse_response[len(ref_signal):]

    # File saveas dialog
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".wav", title="Save Impulse Response as Wave File")

    print("Your IR is ready at: " + file_path)
    sf.write(file_path, impulse_response, sr)

def plotFig():
    
    # Global parameters initialized
    global impulse_response, sr, file_path

    melSpec_IR = rosa.feature.melspectrogram(y=impulse_response, sr=sr, n_fft=2048, hop_length=512, n_mels=128)
    Normalized_melSpec_IR = rosa.power_to_db(S=melSpec_IR, ref=np.max)

    # Setup the figure and subplots
    fig = plt.figure(figsize=(20, 10))
    grid = gridspec.GridSpec(2, 1, figure=fig)
    
    ax1 = fig.add_subplot(grid[0, 0])
    ax2 = fig.add_subplot(grid[1, 0])

    # Plot impulse response waveform
    ax1.plot(impulse_response)
    ax1.set_title("Impulse Response Waveform")
    ax1.set_xlabel("Sample")
    ax1.set_ylabel("Amplitude")

    # Plot impulse response mel spectrogram
    rosa.display.specshow(Normalized_melSpec_IR, sr=sr, hop_length=512, x_axis='time', y_axis='mel', ax=ax2)
    ax2.set_title("Impulse Response Mel Spectrogram")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Frequency")
    #plt.colorbar(mappable=ax2.collections[0], ax=ax2, format='%+2.0f dB')

    # Save the figure
    modified_filepath = file_path[:-4]
    plt.savefig(modified_filepath + ".png")
    plt.close()

if __name__ == "__main__":
    main()