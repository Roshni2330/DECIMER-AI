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