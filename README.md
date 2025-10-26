# YouTube a MP3

Este proyecto permite **descargar videos de YouTube como archivos MP3** con la máxima calidad.  
Incluye dos formas de uso: desde el código fuente en Python o usando un **ejecutable listo** para Windows.

---

## Contenido del repositorio

<<<<<<< HEAD
- `youtube.py` → Código fuente en Python.  
- `ffmpeg.exe` → Necesario para convertir videos a MP3.  
- `proyecto_completo.zip` → Ejecutable listo para usar (`youtube.exe` + `ffmpeg.exe`).  
- `README.md` → Instrucciones de instalación y uso.  
=======
- `youtube.py` → Código fuente en Python.
- `ffmpeg.exe` → Necesario para convertir videos a MP3.
- `proyecto_completo.zip` → Ejecutable listo para usar (`youtube.exe` + `ffmpeg.exe`).
- `README.md` → Instrucciones de instalación y uso.
>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191

---

## Opción 1: Usar el ZIP (ejecutable listo para Windows)

<<<<<<< HEAD
1. Descarga y extrae `proyecto_completo.zip` en cualquier carpeta.  
=======
1. Descarga y extrae `proyecto_completo.zip` en cualquier carpeta.
>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191
2. Asegúrate de que los archivos dentro de la carpeta sean:

youtube.exe
ffmpeg.exe


<<<<<<< HEAD
3. Abre la carpeta dist y haz doble clic en `youtube.exe` para abrir la aplicación.  
4. En la ventana que aparece:  
- Ingresa la URL del video de YouTube que quieras descargar.  
- Haz clic en **Descargar MP3**.  
- Espera a que termine la descarga y conversión (verás la barra de progreso).  
5. El archivo MP3 se guardará automáticamente en la carpeta **Descargas** de tu PC.  
=======
3. Haz doble clic en `youtube.exe` para abrir la aplicación.
4. En la ventana que aparece:
   - Ingresa la URL del video de YouTube que quieras descargar.
   - Haz clic en **Descargar MP3**.
   - Espera a que termine la descarga y conversión (verás la barra de progreso).
5. El MP3 se guardará automáticamente en la carpeta **Descargas** de tu PC.
>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191

---

## Opción 2: Ejecutar desde el código fuente (`youtube.py`)

### Requisitos

<<<<<<< HEAD
- Windows con Python 3.10 o superior.  
- Conexión a Internet.  
- Dependencias de Python: `yt-dlp` y `tk`.  

---
=======
- Windows con Python 3.10 o superior.
- Conexión a Internet.
- Dependencias de Python: `yt-dlp` y `tk`.
>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191

### Paso 1: Instalar Python

1. Descarga Python desde [python.org](https://www.python.org/downloads/windows/).  
<<<<<<< HEAD
2. Durante la instalación, **marca la opción "Add Python to PATH"**.  
3. Verifica la instalación en PowerShell o CMD:  

```powershell
python --version

Debe mostrar algo como:

Python 3.12.x

Paso 2: Instalar dependencias
Abre PowerShell o CMD en la carpeta del proyecto y ejecuta:

=======
2. Durante la instalación, **marca la opción "Add Python to PATH"**.
3. Verifica la instalación en PowerShell o CMD:
   ```powershell
   python --version

Debe mostrar algo como Python 3.12.x.

Paso 2: Instalar dependencias
Abre PowerShell o CMD en la carpeta del proyecto y ejecuta:
>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191
python -m pip install yt-dlp tk

Esto instalará todas las librerías necesarias.

Paso 3: Asegurarte de tener ffmpeg
<<<<<<< HEAD

Debes tener ffmpeg.exe en la misma carpeta que youtube.py.

Si no lo tienes, descárgalo desde:
https://www.gyan.dev/ffmpeg/builds/#release-builds

→ Elige ffmpeg-release-essentials.zip
→ Extrae ffmpeg.exe y colócalo junto a youtube.py.
=======
-Debes tener ffmpeg.exe en la misma carpeta que youtube.py.
-Puedes descargarlo aquí: https://www.gyan.dev/ffmpeg/builds/#release-builds
 → elegir ffmpeg-release-essentials.zip → extraer ffmpeg.exe.
>>>>>>> 0e472698900c145d98b4d4f36e46ed7368c72191

Paso 4: Ejecutar el programa
En la carpeta del proyecto, ejecuta:
python youtube.py

Se abrirá la ventana de la aplicación con el mismo funcionamiento que el ejecutable.

<<<<<<< HEAD
- Detalles de funcionamiento

- La aplicación convierte automáticamente los videos a MP3 con calidad 320 kbps.

- La barra de progreso muestra el estado de la descarga.

- Los archivos se guardan en la carpeta Descargas del usuario.

- El nombre del archivo es exactamente el título del video en YouTube.



*** ESTE PROYECTO FUE REALIZADO POR MI: SebasPazmi: https://github.com/SebasPazmi ***

=======
Detalles de funcionamiento

-La aplicación convierte automáticamente los videos a MP3 con calidad 320 kbps.
-La barra de progreso muestra el estado de la descarga.
-Los archivos se guardan en la carpeta Descargas del usuario.
-El nombre del archivo es exactamente el título del video de YouTube.

ADICIONAL:
¿Cómo convertir el archivo .py en un .exe?

-Con el siguiente comando en terminal: pyinstaller --onefile --windowed --add-binary "ffmpeg.exe;." youtube.py



*** ESTE PROYECTO FUE REALIZADO POR MI: SebasPazmi: https://github.com/SebasPazmi ***