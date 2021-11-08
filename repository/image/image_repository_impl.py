import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from repository.configs import *
from repository.image.image_repository import ImageRepository
from utils.date_translator import getDateInString

class ImageGenerationRepositoryImplementation(ImageRepository):

    def __init__(self):
        self.text_color = TEXT_COLOR
        self.text_font = ImageFont.truetype(TEXT_FONT_FAMILY, TEXT_FONT_SIZE)

    def generateSubjectTicket(self, description: str, user_file_name: str):
        final_text = ""

        im = Image.open(BASE_FILE_NAME)

        draw = ImageDraw.Draw(im)

        lines = textwrap.wrap(description, 75, initial_indent='\r\r\r\r')

        for idx, line in enumerate(lines):
            line += str('\n')
            final_text += line

        self._draw_multi_line_text(draw, final_text)
        self._draw_date(draw)
        self._draw_cpf(draw)

        file_path = self._generate_file_name_and_save(im, user_file_name)
        self._create_pdf(file_path, user_file_name)
        self._remove_png(user_file_name)

    def _draw_multi_line_text(self, draw: ImageDraw, final_text: str):
        xy = (120, 165)
        draw.multiline_text(xy, final_text, self.text_color, self.text_font, spacing=15)

    def _draw_date(self, draw: ImageDraw):
        date = getDateInString()
        xy = (150, 320)
        draw.text(xy, date, self.text_color, self.text_font)

    def _draw_cpf(self, draw: ImageDraw):
        xy = (520, 460)
        draw.text(xy, CPF, self.text_color, self.text_font)

    @staticmethod
    def _generate_file_name_and_save(im: Image, user_file_name: str):
        file_path = f"{user_file_name}.png"
        im.save(file_path)
        return file_path

    @staticmethod
    def _create_pdf(file_path: str, user_file_name: str):
        pdf = Image.open(file_path).convert("RGB")
        pdf.save(f"{user_file_name}.pdf")

    @staticmethod
    def _remove_png(user_file_name: str):
        os.remove(f"{user_file_name}.png")
