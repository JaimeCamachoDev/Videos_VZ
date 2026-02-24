<header>

![Banner](https://github.com/user-attachments/assets/5b933a56-0ece-452a-99c0-1a641485a6b9)

# **Videos_VZ**

_**Montador de Videos para VZ**_

</header>

## Uso rápido: composición automática `A + X + B + Y + C`

Este repo incluye un script para generar vídeos con estructura fija:

1. Entradilla fija `A`
2. 10 segundos de vídeo variable `X`
3. Nudo fijo `B`
4. 10 segundos de vídeo variable `Y`
5. Cierre fijo `C`

### Requisitos

- Python 3.10+
- `ffmpeg` instalado y disponible en `PATH`

### Comando

```bash
python3 compose_video.py \
  --a media/A.mp4 \
  --x media/X_unico.mp4 \
  --b media/B.mp4 \
  --y media/Y_unico.mp4 \
  --c media/C.mp4 \
  --output output/video_final.mp4
```

### Qué hace internamente

- Recorta `X` y `Y` a **10 segundos**.
- Normaliza todos los clips a formato compatible para unirlos.
- Concatena en orden `A + X + B + Y + C`.
- Exporta un `.mp4` final automáticamente.

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
