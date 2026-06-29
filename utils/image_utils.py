from pathlib import Path
from PIL import Image


class ImageUtils:

    @staticmethod
    def save_image(image, path):

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        image.save(path)

        return path

    @staticmethod
    def open_image(path):

        return Image.open(path)