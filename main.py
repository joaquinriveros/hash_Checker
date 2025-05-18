import tkinter as tk
from tkinter import filedialog
from utils import calculate_hashes, save_log, process_folder

def select_file():
    path = filedialog.askopenfilename(title="Selecciona un archivo")
    if not path:
        return
    hashes = calculate_hashes(path)
    result_text.set("\n".join(f"{k.upper()}: {v}" for k, v in hashes.items()))
    save_log(path, hashes)

# Interfaz
root = tk.Tk()
root.title("Calculadora de Hash")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Calculadora de Hashes (MD5, SHA-1, SHA-256)", font=("Arial", 14)).pack(pady=10)

tk.Button(frame, text="Seleccionar archivo", command=select_file).pack(pady=5)
tk.Button(frame, text="Seleccionar carpeta", command=process_folder).pack(pady=5)

result_text = tk.StringVar()
tk.Label(frame, textvariable=result_text, justify="left", wraplength=500).pack(pady=10)

root.mainloop()
