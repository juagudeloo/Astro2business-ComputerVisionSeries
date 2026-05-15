# Visión por Computadora con YOLO — Serie 1 · Computer Vision with YOLO — Series 1

> Parte del canal de YouTube **[Datos de Ciencia](https://youtube.com/@DatosDeCiencia)** ·
> Part of the **[Datos de Ciencia](https://youtube.com/@DatosDeCiencia)** YouTube channel

**Autor / Author:** Juan Esteban Agudelo Ortiz  
**GitHub personal:** [github.com/juagudeloo](https://github.com/juagudeloo) · **Org:** [DatosDeCiencia-LAT](https://github.com/DatosDeCiencia-LAT)  
**Contacto / Contact:** juan.es.agor@gmail.com

---

## Español

### Sobre el canal

**Datos de Ciencia** es un canal de YouTube en español creado por Juan Esteban Agudelo Ortiz. Su tesis central es que los investigadores científicos desarrollan habilidades directamente transferibles a la industria, y que la inversión en ciencia genera capacidad industrial. El canal no es exclusivo de la astrofísica — está abierto a cualquier campo científico que permita ilustrar esta idea.

El contenido se organiza en dos direcciones:

- **Dirección A (Industria → Ciencia):** se toma una técnica dominante en la industria, se demuestra primero en su contexto industrial original y luego se aplica a un conjunto de datos científico. El espectador ve que el método es el mismo; lo que cambia es el dominio.
- **Dirección B (Ciencia → Industria):** se toma una técnica que nació o se desarrolló principalmente en el ámbito científico, se muestra en ese contexto y luego se traza su análogo en la industria.

### Esta serie: Visión por Computadora con YOLO

Primera serie del canal, **Dirección A**. YOLO (*You Only Look Once*) es el estándar de detección de objetos en tiempo real en la industria. La serie lo demuestra primero en imágenes de drones aéreos (caso industrial, VisDrone) y luego en imágenes del Sol capturadas por el satélite SDO de la NASA (caso científico, dataset LSDO).

La teoría se deja para el final para que el espectador ya tenga intuición práctica antes de entender los detalles internos de la arquitectura.

| Video | Contenido | Carpeta | Estado |
|---|---|---|---|
| Intro | Presentación del canal | — | Listo para grabar |
| Baseline | Evaluación zero-shot de YOLO11 sobre VisDrone. Establece la línea base y demuestra el concepto de *domain shift*. | `1-Yolo_baseline/` | ✅ Publicado |
| Fine-tuning VisDrone | Ajuste fino de YOLO11 sobre VisDrone para superar la línea base. Transfer learning, congelamiento de capas, calibración de umbral. | `2-fine-tuning/` | ⬜ Pendiente |
| Fine-tuning Solar | Ajuste fino sobre una muestra del dataset LSDO (imágenes del Sol del SDO con *bounding boxes* de estructuras solares). Video exploratorio. | `3-Yolo_solar_data-SDO/` | ⬜ Pendiente |
| MLOps | El modelo ajustado se despliega como API REST, se conteneriza con Docker, se monta en la nube y se configura monitoreo. | *(carpeta por crear)* | ⬜ Pendiente |
| Teoría YOLO | Cómo funciona YOLO por dentro: grilla SxS, vector de predicción por celda, *bounding boxes*, NMS. Animaciones en Manim. | `5-Yolo_theory/` | ⬜ Pendiente |

### Cómo empezar

Los notebooks son autocontenidos: bajan los datos y los pesos del modelo automáticamente. Sigue los videos en orden — cada episodio construye sobre el anterior.

**Requisitos:** Python 3.12, PyTorch con CUDA recomendado (los notebooks corren en CPU también, pero más lento).

```bash
# Instalar dependencias
pip install ultralytics manim shapely opencv-python matplotlib pandas scikit-learn Pillow requests

# Abrir los notebooks
jupyter lab

# Renderizar la animación de teoría (baja calidad para preview)
manim -pql 5-Yolo_theory/yolo_grid_animation.py YOLOGridAnimation
```

### Política de idioma

- **Videos (narración y diapositivas):** en español.
- **Notebooks:** en inglés, para que funcionen como referencias técnicas autónomas con el mayor alcance posible.

---

## English

### About the channel

**Datos de Ciencia** is a Spanish-language YouTube channel created by Juan Esteban Agudelo Ortiz. Its central thesis: scientific researchers develop skills that are directly transferable to industry, and investing in science produces industrial capability. The channel is not restricted to astrophysics — it is open to any scientific field that can illustrate this idea.

Content is organized around two directions:

- **Direction A (Industry → Science):** a technique dominant in industry is demonstrated in its original industrial context first, then applied to a scientific dataset. The viewer sees that the method is the same; what changes is the domain.
- **Direction B (Science → Industry):** a technique that originated or was heavily developed in a scientific context is shown there first, then its industrial analog is traced.

### This series: Computer Vision with YOLO

The channel's first series follows **Direction A**. YOLO (*You Only Look Once*) is the industry standard for real-time object detection. The series demonstrates it first on aerial drone imagery (the industrial case, VisDrone dataset) and then on solar imagery from NASA's SDO satellite (the scientific case, LSDO dataset).

Theory is intentionally placed last — by then the viewer already has practical intuition before diving into the internal architecture.

| Episode | Content | Folder | Status |
|---|---|---|---|
| Intro | Channel introduction | — | Ready to record |
| Baseline | Zero-shot YOLO11 evaluation on VisDrone. Establishes the baseline and demonstrates *domain shift* concretely. | `1-Yolo_baseline/` | ✅ Published |
| Fine-tuning VisDrone | Fine-tuning YOLO11 on VisDrone to close the gap established in the baseline. Transfer learning, layer freezing, threshold calibration. | `2-fine-tuning/` | ⬜ Pending |
| Fine-tuning Solar | Same fine-tuning approach applied to a sample of the LSDO dataset (SDO solar images with bounding boxes over solar structures). Explicitly exploratory. | `3-Yolo_solar_data-SDO/` | ⬜ Pending |
| MLOps | The fine-tuned model deployed as a REST API, containerized with Docker, mounted on cloud infrastructure, with monitoring. | *(folder to be created)* | ⬜ Pending |
| YOLO Theory | How YOLO works internally: SxS grid, per-cell prediction vector, bounding boxes, NMS. Manim animations, no live coding. | `5-Yolo_theory/` | ⬜ Pending |

### Getting started

Notebooks are self-contained: they download datasets and model weights automatically. Follow the episodes in order — each one builds on the previous.

**Requirements:** Python 3.12, CUDA-capable GPU recommended (notebooks also run on CPU, just slower).

```bash
# Install dependencies
pip install ultralytics manim shapely opencv-python matplotlib pandas scikit-learn Pillow requests

# Open the notebooks
jupyter lab

# Render the theory animation (low quality preview)
manim -pql 5-Yolo_theory/yolo_grid_animation.py YOLOGridAnimation
```

### Language policy

- **Videos (narration and slides):** in Spanish, to maximize access for the Spanish-speaking science and technology community.
- **Notebooks:** in English, so they function as standalone technical references with the broadest possible reach.

---

## Repository structure

```
.
├── 1-Yolo_baseline/        # Zero-shot evaluation notebook (Published)
├── 2-fine-tuning/          # Fine-tuning on VisDrone (Pending)
├── 3-Yolo_solar_data-SDO/  # Fine-tuning on SDO solar data (Pending)
└── 5-Yolo_theory/          # Manim animation script for YOLO theory (Pending)
```

Datasets, model weights, and render outputs are excluded from version control (see `.gitignore`). All notebooks include instructions for downloading the required data programmatically.

---

*Juan Esteban Agudelo Ortiz · [github.com/juagudeloo](https://github.com/juagudeloo) · juan.es.agor@gmail.com*
