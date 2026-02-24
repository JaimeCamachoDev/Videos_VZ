<header>

![Banner](https://github.com/user-attachments/assets/5b933a56-0ece-452a-99c0-1a641485a6b9)

# **Videos_VZ**

_**Montador de Videos para VZ**_

</header>

## Qué hace este proyecto

Genera automáticamente un vídeo final con esta estructura fija:

`A + 10 segundos de X + B + 10 segundos de Y + C`

- `A`, `B`, `C`: clips fijos que se repiten siempre.
- `X`, `Y`: clips variables que cambian en cada vídeo.

---

## Guía paso a paso (desde cero)

### 1) Instalar lo necesario

Necesitas:
- **Python 3.10 o superior**
- **ffmpeg** (imprescindible)

Comandos típicos para instalar `ffmpeg`:

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install -y ffmpeg

# macOS (Homebrew)
brew install ffmpeg

# Windows (winget)
winget install Gyan.FFmpeg
```

Verifica que todo está bien:

```bash
python3 --version
ffmpeg -version
```

---

### 2) Preparar tus archivos de vídeo

Crea una carpeta `media/` y mete ahí tus vídeos, por ejemplo:

- `media/A.mp4` (entradilla fija)
- `media/B.mp4` (nudo fijo)
- `media/C.mp4` (cierre fijo)
- `media/X_001.mp4` (clip variable X)
- `media/Y_001.mp4` (clip variable Y)

> El script recorta automáticamente **X** e **Y** a 10 segundos.

---

### 3) Ejecutar el script

Desde la raíz del proyecto (`Videos_VZ`), lanza:

```bash
python3 compose_video.py \
  --a media/A.mp4 \
  --x media/X_001.mp4 \
  --b media/B.mp4 \
  --y media/Y_001.mp4 \
  --c media/C.mp4 \
  --output output/video_final_001.mp4
```

Si todo va bien, verás algo como:

```text
Vídeo creado: output/video_final_001.mp4
```

---

### 4) Repetir para nuevos vídeos (rápido)

Para cada vídeo nuevo:
- mantienes `A`, `B`, `C` iguales,
- solo cambias `X` y `Y`,
- y cambias el nombre del `--output`.

Ejemplo:

```bash
python3 compose_video.py \
  --a media/A.mp4 \
  --x media/X_002.mp4 \
  --b media/B.mp4 \
  --y media/Y_002.mp4 \
  --c media/C.mp4 \
  --output output/video_final_002.mp4
```

---

## Qué hace internamente el script

- Recorta `X` y `Y` a **10 segundos**.
- Normaliza todos los clips para que tengan formato compatible (1080p, 30fps, H.264/AAC).
- Concatena en orden: `A + X + B + Y + C`.
- Exporta un `.mp4` final.

---

## Problemas típicos y solución

- **`ffmpeg no está instalado o no está en PATH`**
  - Instala ffmpeg y vuelve a abrir la terminal.

- **`No se encontró X: ...` (o A/B/C/Y)**
  - Revisa rutas y nombres de archivos.

- **Vídeo tarda en procesar**
  - Es normal al recodificar. Depende de duración y potencia del equipo.

<footer>

## Después de crear el repositorio desde la plantilla, asegúrate de revisar lo siguiente:

### 📸 Social Preview
- [ ] Sube una imagen `preview.png` personalizada en `Settings → Social Preview`.

### ⚙️ Repository Features
Desactiva funciones que no necesitas en `Settings → Features`:

- [ ] Desactivar **Projects**
- [ ] Desactivar **Wiki**
- [ ] Desactivar **Packages**
- [ ] Desactivar **Environments** (Deployments)
- [ ] Confirmar que **Releases** sigue activado ✅

### 🎨 Personalización visual
- [ ] Cambiar imagen del banner de portada.
- [ ] Dejar Topics necesarios.

</footer>
