import librosa as rosa
import numpy as np
import soundfile as sf
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

class SignalProcess:
    def __init__(self):
        self.sr = None
        self.impulse_response = None
        self.file_path = None

    def signalProcess(self, reference_path, recorded_path, output_path):

        # Loading reference and recorded file
        ref_signal, self.sr = rosa.load(reference_path, sr=None, mono=True)
        rec_signal, _ = rosa.load(recorded_path, sr=self.sr, mono=True)

        # Deconvolution signal processing
        self.impulse_response = fftconvolve(rec_signal, ref_signal[::-1], mode='full')
        self.impulse_response /= np.abs(self.impulse_response).max()
        self.impulse_response = self.impulse_response[len(ref_signal):]

        # Save wav file
        self.file_path = output_path
        sf.write(self.file_path, self.impulse_response, self.sr)

    def plotFig(self):
        # Ensure impulse_response is not None and contains data
        if self.file_path and self.impulse_response is not None and len(self.impulse_response) > 0:
            melSpec_IR = rosa.feature.melspectrogram(y=self.impulse_response, sr=self.sr, n_fft=2048, hop_length=512, n_mels=128)
            Normalized_melSpec_IR = rosa.power_to_db(S=melSpec_IR, ref=np.max)

            fig = plt.figure(figsize=(20, 10))
            grid = gridspec.GridSpec(2, 1, figure=fig)

            ax1 = fig.add_subplot(grid[0, 0])
            ax2 = fig.add_subplot(grid[1, 0])

            ax1.plot(self.impulse_response)
            ax1.set_title("Impulse Response Waveform")
            ax1.set_xlabel("Sample")
            ax1.set_ylabel("Amplitude")

            rosa.display.specshow(Normalized_melSpec_IR, sr=self.sr, hop_length=512, x_axis='time', y_axis='mel', ax=ax2)
            ax2.set_title("Impulse Response Mel Spectrogram")
            ax2.set_xlabel("Time")
            ax2.set_ylabel("Frequency")

            modified_filepath = self.file_path[:-4] + ".png"
            plt.savefig(modified_filepath)
            plt.close()
        else:
            print("Missing impulse response or file path. Please run the signal process first.")
