import hashlib
from datetime import datetime
import os
from tkinter import filedialog, messagebox

ALGORITHMS = ['md5', 'sha1', 'sha256']

def calculate_hashes(file_path):
    hashes = {}
    for algo in ALGORITHMS:
        h = hashlib.new(algo)
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                h.update(chunk)
        hashes[algo] = h.hexdigest()
    return hashes

def save_log(file_path, hashes, folder=None, log_file=None, append=False):
    if not folder:
        folder = filedialog.askdirectory(title="Selecciona una carpeta para guardar el log")
        if not folder:
            return

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = log_file if log_file else f"log_{now}.txt"
    full_path = os.path.join(folder, filename)

    mode = 'a' if append else 'w'
    with open(full_path, mode) as log:
        log.write(f"\n{'-'*50}\n")
        log.write(f"Archivo: {os.path.basename(file_path)}\n")
        log.write(f"Ruta: {file_path}\n")
        log.write(f"Fecha y hora: {datetime.now()}\n")
        for algo, hash_val in hashes.items():
            log.write(f"{algo.upper()}: {hash_val}\n")
    
    if not append:
        messagebox.showinfo("Guardado", f"Log guardado en:\n{full_path}")
    
    return full_path  # Para que podamos seguir escribiendo si es un lote

def process_folder():
    folder_path = filedialog.askdirectory(title="Selecciona una carpeta para escanear")
    if not folder_path:
        return

    log_folder = filedialog.askdirectory(title="Selecciona una carpeta para guardar el log")
    if not log_folder:
        return

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"log_folder_{now}.txt"
    full_log_path = None

    total = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                hashes = calculate_hashes(file_path)
                full_log_path = save_log(file_path, hashes, folder=log_folder, log_file=log_file, append=True)
                total += 1
            except Exception as e:
                print(f"Error procesando {file_path}: {e}")

    if total > 0 and full_log_path:
        messagebox.showinfo("Completado", f"Se procesaron {total} archivos.\nLog en:\n{full_log_path}")
    else:
        messagebox.showwarning("Sin archivos", "No se encontraron archivos para procesar.")
