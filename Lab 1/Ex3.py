# 3. Use the AI to design an application with a GUI that is able to integrate your algorithm from
# assignement 1 and 2. Your application must have a button which allows the user to choose a Fasta File.
# Fasta Files contain a specific biological format. The output should be shown on the main window by using
# a text box object or something similar. Fasta Files have the following format:
#  I. The first line is the information line that shows the ID of the sequence, the species and other of info
#  II. Starting from the second line we have the raw sequence which can be DNA, RNA or proteins that is split
# in 80 character lines until the end of the file
# Use the AI to simulate a fasta file for your input

import tkinter as tk
from tkinter import filedialog, scrolledtext

# ---------------- Algorithm from Assignment 1 ----------------
def find_alphabet(sequence):
    alphabet = []
    for char in sequence:
        if char not in alphabet:
            alphabet.append(char)
    return alphabet

# ---------------- Algorithm from Assignment 2 ----------------
def calculate_frequencies(sequence, alphabet):
    frequencies = {}
    length = len(sequence)
    for char in alphabet:
        count = sequence.count(char)
        relative_frequency = (count / length) * 100
        frequencies[char] = relative_frequency
    return frequencies

# ---------------- Function to read FASTA file ----------------
def read_fasta(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    header = lines[0].strip()       # first line is the info line
    sequence = "".join(line.strip() for line in lines[1:])  # join rest into sequence
    return header, sequence

# ---------------- Main function for button ----------------
def open_fasta():
    filepath = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta *.fa *.txt")])
    if not filepath:
        return
    
    header, sequence = read_fasta(filepath)
    alphabet = find_alphabet(sequence)
    frequencies = calculate_frequencies(sequence, alphabet)

    # Display results
    output_box.delete(1.0, tk.END)  # clear previous text
    output_box.insert(tk.END, f"File: {filepath}\n")
    output_box.insert(tk.END, f"Header: {header}\n\n")
    output_box.insert(tk.END, f"Sequence Length: {len(sequence)}\n")
    output_box.insert(tk.END, f"Alphabet: {alphabet}\n\n")
    output_box.insert(tk.END, "Relative Frequencies:\n")
    for char, freq in frequencies.items():
        output_box.insert(tk.END, f"  {char}: {freq:.2f}%\n")

# ---------------- Tkinter GUI ----------------
root = tk.Tk()
root.title("FASTA Alphabet & Frequency Analyzer")
root.geometry("600x400")

# Button
open_button = tk.Button(root, text="Open FASTA File", command=open_fasta, font=("Arial", 12))
open_button.pack(pady=10)

# Output Box
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Courier", 10))
output_box.pack(padx=10, pady=10)

# Run app
root.mainloop()
