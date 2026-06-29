import hashlib
from pathlib import Path


class HashUtils:

    @staticmethod
    def calculate_sha256(file_path: str | Path) -> str:

        file_path = Path(file_path)

        sha256 = hashlib.sha256()

        with open(file_path, "rb") as file:

            while True:

                chunk = file.read(8192)

                if not chunk:
                    break

                sha256.update(chunk)

        return sha256.hexdigest()