from pathlib import Path

# =====================================================
# PROJECT ROOT
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent

# =====================================================
# FOLDERS
# =====================================================

INPUT_FOLDER = PROJECT_ROOT / "input_pdfs"

DATABASE_FOLDER = PROJECT_ROOT / "database"

RENDERED_FOLDER = PROJECT_ROOT / "rendered_pages"

SEGMENTED_FOLDER = PROJECT_ROOT / "segmented_structures"

CLEANED_FOLDER = PROJECT_ROOT / "cleaned_images"

OUTPUT_FOLDER = PROJECT_ROOT / "outputs"

TEMP_FOLDER = PROJECT_ROOT / "temp"

MODEL_FOLDER = PROJECT_ROOT / "models"

ASSETS_FOLDER = PROJECT_ROOT / "assets"

# =====================================================
# CREATE FOLDERS AUTOMATICALLY
# =====================================================

ALL_FOLDERS = [
    INPUT_FOLDER,
    DATABASE_FOLDER,
    RENDERED_FOLDER,
    SEGMENTED_FOLDER,
    CLEANED_FOLDER,
    OUTPUT_FOLDER,
    TEMP_FOLDER,
    MODEL_FOLDER,
    ASSETS_FOLDER,
]

for folder in ALL_FOLDERS:
    folder.mkdir(parents=True, exist_ok=True)

# =====================================================
# DATABASE FILES
# =====================================================

MASTER_DATABASE = DATABASE_FOLDER / "master_database.csv"

# =====================================================
# IMAGE SETTINGS
# =====================================================

RENDER_DPI = 300

IMAGE_FORMAT = "png"

# =====================================================
# PDF SETTINGS
# =====================================================

SUPPORTED_FORMATS = [".pdf"]

# =====================================================
# APP SETTINGS
# =====================================================

APP_NAME = "DECIMER AI"

VERSION = "2.0"