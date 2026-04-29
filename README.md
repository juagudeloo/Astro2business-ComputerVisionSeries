# Visión por Computadora con YOLO — Serie 1 · Computer Vision with YOLO — Series 1

> Parte del canal de YouTube **[Datos de Ciencia](https://youtube.com/@DatosDeCiencia)** ·
> Part of the **[Datos de Ciencia](https://youtube.com/@DatosDeCiencia)** YouTube channel

**Autor / Author:** Juan Esteban Agudelo Ortiz · juan.es.agor@gmail.com  
**Organización / Organization:** [DatosDeCiencia-LAT](https://github.com/DatosDeCiencia-LAT)

---

## Español

### Sobre el canal

**Datos de Ciencia** es un canal de YouTube que existe para demostrar una tesis sencilla: los investigadores científicos desarrollan habilidades que son directamente transferibles a la industria, y la inversión en ciencia genera capacidad industrial. El canal no es exclusivo de la astrofísica — está abierto a cualquier campo científico que permita ilustrar esta idea.

El contenido se organiza en dos direcciones:

- **Dirección A (Industria → Ciencia):** se toma una técnica dominante en la industria, se demuestra primero en su contexto industrial original y luego se aplica a un conjunto de datos científico. El espectador ve que el método es el mismo; lo que cambia es el dominio.

- **Dirección B (Ciencia → Industria):** se toma una técnica que nació o se desarrolló principalmente en el ámbito científico, se muestra en ese contexto y luego se traza su análogo en la industria. El espectador ve que la ciencia produce herramientas con valor práctico.

### Esta serie: Visión por Computadora con YOLO

Esta es la primera serie del canal y corresponde a la **Dirección A**. YOLO (*You Only Look Once*) es el estándar de detección de objetos en tiempo real en la industria. La serie lo demuestra primero en imágenes de drones (caso industrial) y luego en datos de física solar (caso científico).

| # | Contenido | Artefactos |
|---|---|---|
| 1 | **Teoría de YOLO** — Cómo funciona YOLO: la grilla SxS, el vector de predicción por celda, los *bounding boxes* y la supresión de máximos no locales. Animaciones generadas con Manim. | Notebook · Script de video |
| 2 | **Inferencia zero-shot sobre VisDrone2019-DET** — Se evalúa YOLOv11 preentrenado en COCO sobre el conjunto de validación de VisDrone sin ajuste fino. El objetivo es establecer una línea base y demostrar concretamente el concepto de *domain shift*: el modelo fue entrenado con imágenes a nivel de suelo y se evalúa en imágenes aéreas. | Notebook · Script de video |
| 3 | **Fine-tuning sobre VisDrone2019-DET** — Se ajusta YOLOv11 con los datos de entrenamiento de VisDrone para superar la línea base del video anterior. Se analizan las mejoras por clase y se discuten las estrategias de ajuste. | Notebook · Script de video |
| 4 | **Fine-tuning sobre datos solares SDO (LSDO)** — Se aplica la misma técnica de ajuste fino a una muestra del *dataset* LSDO, que contiene observaciones del Sol del instrumento AIA a bordo del satélite SDO con *bounding boxes* anotados sobre estructuras solares (regiones activas, agujeros coronales, filamentos). Este video es explícitamente exploratorio: el objetivo es mostrar que la técnica es aplicable a imágenes científicas, no producir un modelo publicable. | Notebook · Script de video |
| 5 | **MLOps — Despliegue del modelo como API** — Se toma el modelo ajustado y se despliega como una API REST, se conteneriza con Docker, se monta en infraestructura en la nube y se configura monitoreo. El objetivo es mostrar el ciclo completo desde el experimento hasta la producción. | Notebook · Script de video |

### Política de idioma

- **Videos (narración y diapositivas):** en español, para maximizar el acceso a la comunidad hispanohablante de ciencia y tecnología.
- **Notebooks:** en inglés, para que funcionen como referencias técnicas autónomas con el mayor alcance posible.

---

## English

### About the channel

**Datos de Ciencia** is a YouTube channel built around a single thesis: scientific researchers develop skills that are directly transferable to industry, and investing in science produces industrial capability. The channel is not restricted to astrophysics — it is open to any scientific field that can illustrate this idea.

Content is organized around two directions:

- **Direction A (Industry → Science):** a technique dominant in industry is demonstrated in its original industrial context first, then applied to a scientific dataset. The viewer sees that the method is the same; what changes is the domain.

- **Direction B (Science → Industry):** a technique that originated or was heavily developed in a scientific context is shown there first, then its industrial analog is traced. The viewer sees that science produces tools with practical value.

### This series: Computer Vision with YOLO

This is the channel's first series and follows **Direction A**. YOLO (*You Only Look Once*) is the industry standard for real-time object detection. The series demonstrates it first on drone imagery (the industrial case) and then on solar physics data (the scientific case).

| # | Content | Artifacts |
|---|---|---|
| 1 | **YOLO Theory** — How YOLO works: the SxS grid, the per-cell prediction vector, bounding boxes, and non-maximum suppression. Animations produced with Manim. | Notebook · Video script |
| 2 | **Zero-shot inference on VisDrone2019-DET** — YOLOv11 pretrained on COCO is evaluated on the VisDrone validation set with no fine-tuning. The goal is to establish a baseline and concretely demonstrate *domain shift*: the model was trained on ground-level imagery and is evaluated on aerial imagery. | Notebook · Video script |
| 3 | **Fine-tuning on VisDrone2019-DET** — YOLOv11 is fine-tuned on the VisDrone training split to improve over the baseline from the previous video. Per-class improvements are analyzed and tuning strategies are discussed. | Notebook · Video script |
| 4 | **Fine-tuning on solar SDO data (LSDO)** — The same fine-tuning approach is applied to a sample of the LSDO dataset, which contains Solar Dynamics Observatory AIA observations with annotated bounding boxes over solar structures (active regions, coronal holes, filaments). This video is explicitly exploratory: the goal is to demonstrate that the technique transfers to scientific imaging, not to produce a publication-ready model. | Notebook · Video script |
| 5 | **MLOps — Deploying the model as an API** — The fine-tuned model is deployed as a REST API, containerized with Docker, mounted on cloud infrastructure, and monitoring is configured. The goal is to show the full cycle from experiment to production. | Notebook · Video script |

### Language policy

- **Videos (narration and slides):** in Spanish, to maximize access for the Spanish-speaking science and technology community.
- **Notebooks:** in English, so they function as standalone technical references with the broadest possible reach.

---

## Repository structure

```
.
├── 1-Yolo_theory/          # Manim animation script
├── 2-Yolo_baseline/        # Zero-shot evaluation notebook
├── 3-Yolo_finetuned/       # Fine-tuning on VisDrone
├── 4-Yolo_solar_data-SDO/  # Fine-tuning on SDO solar data
└── 5-Yolo_MLOps/           # Deployment and monitoring
```

Datasets, model weights, and render outputs are excluded from version control (see `.gitignore`). All notebooks include instructions for downloading the required data programmatically.

---

*Juan Esteban Agudelo Ortiz · juan.es.agor@gmail.com*
