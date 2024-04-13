import tkinter as tk
from tkinter import filedialog, messagebox
from Deconvolution import SignalProcess

class AudioProcessorGUI:

    def __init__(self, master):
        self.master = master
        master.title("Deconvolution Tool")
        master.geometry("600x400")

        # Create an instance of the SignalProcess class
        self.processor = SignalProcess()

        # Initialize file paths
        self.reference_path = None
        self.recorded_path = None

        btnRef = tk.Button(master, text="Load Reference File", command=self.loadRef)
        btnRef.pack(pady=20)

        btnRec = tk.Button(master, text="Load Recorded File", command=self.loadRec)
        btnRec.pack(pady=20)

        self.btn_process = tk.Button(master, text="Start Deconvolution", command=self.signalFiles)
        self.btn_process.pack(pady=20)
        self.btn_process["state"] = "disabled"


    def loadRef(self):
        self.reference_path = filedialog.askopenfilename(title="Select Reference Wave File")
        if self.reference_path:
            print(f"Loaded reference file: {self.reference_path}")
            self.check_files_loaded()
        else:
            print("File selection cancelled.")

    def loadRec(self):
        self.recorded_path = filedialog.askopenfilename(title="Select Recorded Wave File")
        if self.recorded_path:
            print(f"Loaded Recorded file: {self.recorded_path}")
            self.check_files_loaded()
        else:
            print("File selection cancelled.")

    def signalFiles(self):
        if self.reference_path and self.recorded_path:
            # File saveas dialog
            output_path = filedialog.asksaveasfilename(defaultextension=".wav", title="Save Impulse Response as Wave File")
            if output_path:
                self.processor.signalProcess(self.reference_path, self.recorded_path, output_path)  # Call processing method
                self.processor.plotFig()  # Call plotting method
                messagebox.showinfo("Processing Complete", "Processing is complete. Check the output files.")
            else:
                messagebox.showerror("File Error", "File saving was cancelled.")
        else:
            messagebox.showerror("File Error", "Please ensure both files are loaded before processing.")
    def check_files_loaded(self):
        if self.reference_path and self.recorded_path:
            self.btn_process["state"] = "normal"
        else:
            self.btn_process["state"] = "disabled"

def main():
    root = tk.Tk()
    app = AudioProcessorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()