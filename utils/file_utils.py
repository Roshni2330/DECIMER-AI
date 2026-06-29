import shutil
from pathlib import Path


class FileUtils:

    @staticmethod
    def copy_file(source, destination):

        source = Path(source)
        destination = Path(destination)

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            source,
            destination
        )

        return destination

    @staticmethod
    def create_folder(folder):

        folder = Path(folder)

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder

    @staticmethod
    def file_exists(path):

        return Path(path).exists()