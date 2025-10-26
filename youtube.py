<<<<<<< HEAD
=======
# youtube.py
>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191
import os
import sys
import tkinter as tk
from tkinter import messagebox, ttk
from pathlib import Path
import yt_dlp

# Carpeta de descargas automática
descargas = str(Path.home() / "Downloads")

# Detectar ruta correcta de ffmpeg
if getattr(sys, 'frozen', False):
    # Ejecutándose desde PyInstaller
    ruta_base = os.path.dirname(sys.executable)
else:
    # Ejecutándose como script normal
    ruta_base = os.path.dirname(__file__)

ffmpeg_path = os.path.join(ruta_base, "ffmpeg.exe")
<<<<<<< HEAD

# Verificar que ffmpeg exista
if not os.path.exists(ffmpeg_path):
    messagebox.showerror("Error", f"No se encontró ffmpeg en: {ffmpeg_path}")
    sys.exit(1)

=======
>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191
# Función de descarga con progreso
def descargar_mp3():
    url = entrada_url.get().strip()

    if not url:
        messagebox.showerror("Error", "Por favor ingresa una URL de YouTube")
        return

    def progreso(d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            descargado = d.get('downloaded_bytes', 0)
            if total:
                porcentaje = int(descargado / total * 100)
                progress_var.set(porcentaje)
                progress_label.config(text=f"{porcentaje}% descargado")
                ventana.update_idletasks()
        elif d['status'] == 'finished':
            progress_var.set(100)
            progress_label.config(text="Descarga completada. Convirtiendo a MP3...")

    try:
        opciones = {
<<<<<<< HEAD
            "ffmpeg_location": ffmpeg_path,
            # Intentar m4a primero, luego el mejor audio posible
            "format": "bestaudio[ext=m4a]/bestaudio/best",
            "noplaylist": True,
            "outtmpl": os.path.join(descargas, "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }],
            "progress_hooks": [progreso],
        }
=======
    "ffmpeg_location": ffmpeg_path,
    "format": "bestaudio/best",
    "noplaylist": True,
    "outtmpl": os.path.join(descargas, "%(title)s.%(ext)s"),
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "320",
    }],
    "progress_hooks": [progreso],
}

>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191

        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        messagebox.showinfo("Éxito", f"Descarga completada en:\n{descargas}")
        progress_var.set(0)
        progress_label.config(text="")

    except Exception as e:
<<<<<<< HEAD
        messagebox.showerror("Error", f"Ocurrió un problema:\n{str(e)}")
=======
        messagebox.showerror("Error", str(e))
>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191
        progress_var.set(0)
        progress_label.config(text="")

# Interfaz Tkinter
ventana = tk.Tk()
ventana.title("YouTube a MP3 (con progreso)")
ventana.geometry("500x250")

tk.Label(ventana, text="URL de YouTube:", font=("Arial", 12)).pack(pady=10)
entrada_url = tk.Entry(ventana, width=60)
entrada_url.pack(pady=5)

tk.Button(
    ventana,
    text="Descargar MP3",
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=descargar_mp3
).pack(pady=10)

# Barra de progreso
progress_var = tk.IntVar()
progressbar = ttk.Progressbar(ventana, maximum=100, variable=progress_var, length=400)
progressbar.pack(pady=10)

progress_label = tk.Label(ventana, text="")
progress_label.pack()

ventana.mainloop()
