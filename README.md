# Audio Signal Processing Tool

This Python script calculates the deconvolution of audio signals to extract the impulse response from a recorded audio file using a reference file. It uses the `librosa`, `numpy`, `soundfile`, and `scipy` libraries for signal processing and the `tkinter` library for file dialogues.

## Requirements

- Python 3
- librosa
- numpy
- soundfile
- scipy
- tkinter

## Usage

1. Run the script.
2. When prompted, select your reference audio file through the file dialog.
3. Next, select your recorded audio file.
4. After processing, choose a location and name to save the extracted impulse response as a WAV file.

## Notes

- Ensure that both audio files are accessible and that the script has permission to read/write files.
- The script automatically matches the sampling rate of the recorded audio to that of the reference audio for consistency.
