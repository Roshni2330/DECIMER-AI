import cv2
import numpy as np
from pathlib import Path

from config import CLEANED_FOLDER


class Cleaner:

    def __init__(self):
        pass

    def clean_images(
        self,
        metadata,
        metadata_df
    ):

        output_folder = CLEANED_FOLDER / metadata["doc_id"]

        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        for index in metadata_df.index:

            image_path = Path(
                metadata_df.loc[index, "image_path"]
            )

            image = cv2.imread(str(image_path))

            if image is None:
                continue

            # ============================================
            # Resize large images while keeping aspect ratio
            # ============================================

            h, w = image.shape[:2]

            if max(h, w) > 1200:

                scale = 1200 / max(h, w)

                image = cv2.resize(
                    image,
                    (
                        int(w * scale),
                        int(h * scale)
                    ),
                    interpolation=cv2.INTER_AREA
                )

            # ============================================
            # Noise Removal
            # ============================================

            denoised = cv2.fastNlMeansDenoisingColored(
                image,
                None,
                10,
                10,
                7,
                21
            )

            # ============================================
            # Convert to Grayscale
            # ============================================

            gray = cv2.cvtColor(
                denoised,
                cv2.COLOR_BGR2GRAY
            )

            # ============================================
            # Contrast Enhancement
            # ============================================

            clahe = cv2.createCLAHE(
                clipLimit=2.5,
                tileGridSize=(8, 8)
            )

            gray = clahe.apply(gray)

            # ============================================
            # Sharpen Image
            # ============================================

            kernel = np.array(
                [
                    [0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]
                ]
            )

            sharpened = cv2.filter2D(
                gray,
                -1,
                kernel
            )

            # ============================================
            # Adaptive Threshold
            # ============================================

            cleaned = cv2.adaptiveThreshold(
                sharpened,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                31,
                5
            )

            # ============================================
            # Morphological Cleaning
            # ============================================

            morph_kernel = np.ones(
                (2, 2),
                np.uint8
            )

            cleaned = cv2.morphologyEx(
                cleaned,
                cv2.MORPH_OPEN,
                morph_kernel
            )

            cleaned = cv2.morphologyEx(
                cleaned,
                cv2.MORPH_CLOSE,
                morph_kernel
            )

            # ============================================
            # Save Image
            # ============================================

            cleaned_name = (
                image_path.stem +
                "_clean.png"
            )

            cleaned_path = (
                output_folder /
                cleaned_name
            )

            cv2.imwrite(
                str(cleaned_path),
                cleaned
            )

            # ============================================
            # Update DataFrame
            # ============================================

            metadata_df.loc[
                index,
                "clean_path"
            ] = str(cleaned_path)

        return metadata_df