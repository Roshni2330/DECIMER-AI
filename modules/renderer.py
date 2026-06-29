import fitz
from pathlib import Path

from config import RENDERED_FOLDER, RENDER_DPI


class Renderer:

    def __init__(self):
        pass

    def render_pdf(self, metadata):

        pdf = fitz.open(metadata["pdf_path"])

        doc_id = metadata["doc_id"]

        output_folder = RENDERED_FOLDER / doc_id

        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        zoom = RENDER_DPI / 72

        matrix = fitz.Matrix(zoom, zoom)

        rendered_pages = []

        for page_index in range(len(pdf)):

            page = pdf.load_page(page_index)

            pix = page.get_pixmap(matrix=matrix)

            image_path = output_folder / f"page_{page_index+1:03d}.png"

            pix.save(image_path)

            rendered_pages.append({

                "page_number": page_index + 1,

                "page_path": str(image_path)

            })

        pdf.close()

        return rendered_pages