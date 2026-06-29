from pathlib import Path
from datetime import datetime

from utils.hash_utils import HashUtils
from utils.file_utils import FileUtils

from config import INPUT_FOLDER, DATABASE_FOLDER


class PDFLoader:

    def __init__(self):
        pass

    def generate_doc_id(self):

        metadata_files = list(
            DATABASE_FOLDER.glob("DOC*_metadata.csv")
        )

        return f"DOC{len(metadata_files)+1:03d}"

    def load_pdf(self, pdf_path):

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(pdf_path)

        if pdf_path.suffix.lower() != ".pdf":
            raise ValueError("Only PDF files are supported.")

        doc_id = self.generate_doc_id()

        destination = INPUT_FOLDER / (
            f"{doc_id}_{pdf_path.name}"
        )

        FileUtils.copy_file(
            pdf_path,
            destination
        )

        metadata = {

            "doc_id": doc_id,

            "pdf_name": pdf_path.name,

            "pdf_path": str(destination),

            "pdf_hash": HashUtils.calculate_sha256(destination),

            "processed_on": datetime.now(),

            "processed": False

        }

        return metadata