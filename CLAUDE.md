# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Educational YouTube series ("Astro2business — Computer Vision Series") applying YOLO-based object detection to two domains: aerial drone imagery (VisDrone) and solar astrophysics (SDO Dataverse). Each numbered folder is one episode, roughly in sequence.

| Folder | Episode content |
|---|---|
| `1-Yolo_theory/` | Manim animation explaining the YOLO grid mechanism |
| `2-Yolo_baseline/` | Zero-shot YOLOv11n evaluation on VisDrone2019-DET |
| `3-Yolo_finetuned/` | Fine-tuning on VisDrone (in progress) |
| `4-Yolo_solar_data-SDO/` | YOLO applied to SDO solar-event bounding boxes |
| `5-Yolo_MLOps/` | MLOps / deployment (in progress) |
| `YOLO/` | VisDrone dataset cache — gitignored, auto-populated by Ultralytics |

## Key dependencies

```
ultralytics   # YOLOv11 model, dataset download, val/predict/train API
manim         # animation for episode 1
shapely       # WKT bounding-box parsing (solar episode)
opencv-python numpy matplotlib pandas scikit-learn Pillow requests
```

Python 3.12, PyTorch with CUDA (NVIDIA RTX A4500 in the dev environment).

## Running the Manim animation

```bash
# Preview at low quality (-pql) — renders to media/ (gitignored)
manim -pql 1-Yolo_theory/yolo_grid_animation.py YOLOGridAnimation

# High quality for final render
manim -pqh 1-Yolo_theory/yolo_grid_animation.py YOLOGridAnimation
```

## Running notebooks

```bash
jupyter lab   # or: jupyter notebook
```

Notebooks are self-contained per episode. The VisDrone dataset is downloaded automatically by Ultralytics on first `model.val()` call; SDO data is fetched from the Harvard Dataverse API inside the notebook.

## YOLO API conventions used across notebooks

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")          # weights auto-downloaded if absent

# Evaluation (sweeps full P-R curve internally; conf/iou only affect printed scalars)
results = model.val(data="VisDrone.yaml", imgsz=640, conf=0.25, iou=0.45)

# Inference (conf IS the operational filter here)
results = model.predict(source=img_paths, conf=0.25, iou=0.45, imgsz=640)

# Fine-tuning
model.train(data="sdo.yaml", epochs=50, imgsz=1280, batch=4,
            lr0=1e-4, freeze=10, project="sdo_yolo", name="run1", device="cuda:0")
```

`model.val()` vs `model.predict()`: `conf` behaves differently — AP in `val()` ignores it (sweeps 0.001→1 internally); in `predict()` it is the hard production threshold.

## Dataset formats

**VisDrone**: downloaded via `DATA_CONFIG = "VisDrone.yaml"` — Ultralytics manages the path under `~/.../datasets/VisDrone/`. Labels are 0-indexed to 10 classes: `pedestrian people bicycle car van truck tricycle awning-tricycle bus motor`.

**SDO solar data**: fetched from Harvard Dataverse (`doi:10.7910/DVN/8XRUDT`) as a ZIP, extracted to `../data/sdo_dataverse/`. Bounding boxes are stored as WKT `POLYGON()` strings and must be converted to YOLO normalized format (`cx cy w h` relative to 4096 px). Three event types map to class IDs: `AR→0, FL→1, CH→2`. JP2 images are converted to RGB PNG (grayscale channel triplicated) before training.

## Visual style

All notebooks and the Manim script use a consistent "Datos de Ciencia" palette:
```python
DARK_BG      = "#0D1117"
SOLAR_ORANGE = "#E85D24"
PLASMA_AMBER = "#F5A623"
CORONA_YELLOW = "#FCDE5A"
```
New plots and animations should match this palette.

## Gitignored paths to be aware of

`YOLO/`, `outputs/`, `media/`, `data/`, `runs/`, `*.pt` — none of these should be committed. Model weights are always re-downloaded or trained on the fly.
