import os
from os import path

from PIL import Image


class OSHelper:

    def process_folder_creation(self, file_path: str):
        folders = file_path.split("/")
        del folders[-1]
        self._check_if_folder_exists("/".join(folders))

    @staticmethod
    def create_pdf_file(**kwargs):
        file_path = kwargs.get("file_path")
        file_name = kwargs.get("file_name")
        pdf = Image.open(file_path).convert("RGB")
        pdf.save(f"{file_name}")
        return pdf

    @staticmethod
    def delete_file(file_path: str):
        os.remove(f"{file_path}")

    @staticmethod
    def _check_if_folder_exists(folder: str):
        if not path.exists(folder):
            os.makedirs(folder)
