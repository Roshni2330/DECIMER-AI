<<<<<<< HEAD
# DECIMER AI

## Pipeline

Upload PDF

↓

Duplicate Check

↓

Assign DOC_ID

↓

Render Pages

↓

DECIMER Segmentation

↓

Image Cleaning

↓

Generate SMILES

↓

Statistics

↓

Export CSV

## Output CSV Columns

- doc_id
- pdf_name
- page_number
- image_id
- image_path
- clean_path
- image_type
- is_formula
- smiles
- processed

## Run

```bash
streamlit run app.py
```
=======
# 🧪 DECIMER-AI — Chemical Formula Recognition Pipeline

An AI-powered pipeline that reads chemical formula images and converts them into SMILES notation using DECIMER, with automatic image cleaning and batch processing.

---

## 📌 What Is This Project?

This project takes images of chemical formulas (from books, papers, or photos) and automatically converts them into **SMILES** — a text format that represents chemical structures.

**Example:**
- Input → image of caffeine structure
- Output → `CN1C=NC2=C1C(=O)N(C)C(=O)N2C`

---

## 🚀 Features

- ✅ Single image to SMILES conversion
- ✅ Batch processing — entire folder of images at once
- ✅ Automatic image cleaning (removes scratches, noise, blur, stains)
- ✅ Saves all results to a CSV file
- ✅ Handles real-world damaged/dirty images

---

## 📁 Project Structure

```
DECIMER-AI/
│
├── test001.ipynb          # Main notebook — all code lives here
├── requirements.txt       # All Python packages needed
├── results.csv            # Output file — image paths + SMILES
│
├── molecule.png           # Original test image
├── molecule_clean.png     # Cleaned version of original
│
├── molecule1.png          # Damaged test image 1 (scratched)
├── molecule1_clean.png    # Cleaned version
│
├── molecule2.png          # Damaged test image 2 (stained)
├── molecule2_clean.png    # Cleaned version
│
├── molecule4.png          # Damaged test image 4 (blurry)
├── molecule4_clean.png    # Cleaned version
│
├── molecule5.png          # Damaged test image 5 (photocopy)
└── molecule5_clean.png    # Cleaned version
```

---

## ⚙️ Setup Instructions

### Step 1 — Create Virtual Environment
```bash
python -m venv decimer_env
```

### Step 2 — Activate Environment

Windows:
```bash
decimer_env\Scripts\activate
```

Linux/Mac:
```bash
source decimer_env/bin/activate
```

### Step 3 — Install All Packages
```bash
pip install -r requirements.txt
```

### Step 4 — Open in VS Code
- Open `test001.ipynb`
- Select kernel → `decimer_env`
- Run cells

---

## 🧠 How The Code Works

### 1. Single Image Test
```python
from DECIMER import predict_SMILES

smiles = predict_SMILES(r"C:\path\to\molecule.png")
print(smiles)
```

### 2. Full Pipeline — Clean + Process + Save CSV
```python
# Build the machine
processor = DECIMERProcessor(
    image_folder = r"C:\DECIMER.ai\Decimer.ai\image",
    output_csv   = r"C:\DECIMER.ai\Decimer.ai\results.csv"
)

# Press one button — everything is done
processor.save_to_csv()
```

---

## 🧹 Image Cleaning Pipeline

Real-world images often have:
- ✏️ Scratches and pen marks
- ☕ Tea / coffee stains
- 📄 Crumple / fold lines
- 🌫️ Blur from shaky camera
- 📠 Photocopy noise and streaks

Our cleaning pipeline fixes all of these **before** sending images to DECIMER:

```
Dirty Image
    ↓
Remove noise (OpenCV)
    ↓
Sharpen image (OpenCV)
    ↓
Fix brightness & contrast (PILLOW)
    ↓
Clean Image
    ↓
DECIMER → SMILES ✅
```

---

## 📄 Output CSV Format

After running, `results.csv` will look like:

| image_path | smiles |
|---|---|
| molecule1.png | CN1C=NC2... |
| molecule2.png | CC(=O)Oc1... |
| molecule4.png | C1CCCCC1... |
| molecule5.png | CC(O)... |

---

## 📦 Requirements

| Package | Purpose |
|---|---|
| `decimer` | Chemical formula recognition AI |
| `opencv-python` | Image cleaning — noise, blur, contrast |
| `pillow` | Image sharpening and enhancement |
| `numpy` | Image array processing |
| `ipykernel` | Connects environment to VS Code |

Install all with:
```bash
pip install -r requirements.txt
---
>>>>>>> ec23e814304ede13925961c0b355db8ae765b785
