# Audio Signal Deconvolution Tool

This Python script calculates the deconvolution of audio signals to extract the impulse response from a recorded audio file using a reference file. It uses the `librosa`, `numpy`, `soundfile`, `matplotlib` and `scipy` libraries for signal processing and the `tkinter` library for file dialogues.

## Requirements

- Python 3
- librosa
- numpy
- soundfile
- scipy
- matplotlib
- tkinter

## Installation

To install the required dependencies, you can use pip. Run the following command:

`pip3 install -r requirements.txt`

This will install all the necessary libraries listed in the `requirements.txt` file.

## Usage

1. Run the script.
2. Select your reference audio file through the file dialog.
3. Select your recorded audio file.
4. Choose a location and name to save the extracted impulse response as a WAV file.

## Notes

- Ensure that both audio files are accessible and that the script has permission to read/write files.
- The script automatically matches the sampling rate of the recorded audio to that of the reference audio for consistency.
