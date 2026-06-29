from pathlib import Path

import numpy as np
from PIL import Image

from decimer_segmentation import segment_chemical_structures

from config import SEGMENTED_FOLDER


class Segmentation:

    def __init__(self):
        pass

    def segment_pages(
        self,
        metadata,
        rendered_pages
    ):

        doc_id = metadata["doc_id"]

        output_folder = SEGMENTED_FOLDER / doc_id

        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        image_counter = 1

        segmented_metadata = []

        for page in rendered_pages:

            page_number = page["page_number"]

            image = Image.open(
                page["page_path"]
            )

            # ==========================================
            # Resize huge pages before segmentation
            # ==========================================

            MAX_WIDTH = 2200
            MAX_HEIGHT = 2200

            width, height = image.size

            if width > MAX_WIDTH or height > MAX_HEIGHT:

                scale = min(
                    MAX_WIDTH / width,
                    MAX_HEIGHT / height
                )

                new_width = int(width * scale)
                new_height = int(height * scale)

                image = image.resize(
                    (new_width, new_height),
                    Image.LANCZOS
                )

            print(f"Segmenting Page {page_number} : {image.size}")

            image_np = np.array(image)

            structures = segment_chemical_structures(
                image_np,
                expand=True,
                visualization=False
            )

            for structure in structures:

                image_id = f"IMG{image_counter:05d}"

                save_path = output_folder / f"{image_id}.png"

                Image.fromarray(structure).save(save_path)

                segmented_metadata.append({

                    "doc_id": doc_id,

                    "pdf_name": metadata["pdf_name"],

                    "page_number": page_number,

                    "image_id": image_id,

                    "image_path": str(save_path)

                })

                image_counter += 1

        return segmented_metadata