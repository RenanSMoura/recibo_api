import os
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from repository.image_repository import ImageRepository
from utils.date_translator import getDateInString


class ImageGenerationRepositoryImplementation(ImageRepository):

    def generateSubjectTicket(self, description: str, user_file_name: str, payment_day: str):
        im = Image.open('base_recibo.png')
        draw = ImageDraw.Draw(im)
        text_color = (64, 64, 64)
        font = ImageFont.truetype('Quicksand-Regular.ttf', 18)
        text = description
        date = getDateInString(payment_day)
        lines = textwrap.wrap(text, 75, initial_indent='\r\r\r\r')
        final_text = ""

        for idx, line in enumerate(lines):
            line += str('\n')
            final_text += line

        draw.multiline_text((120, 165), final_text, text_color, font, spacing=15)
        draw.text((150, 320), date, text_color, font)

        cpf_font = ImageFont.truetype('Quicksand-Regular.ttf', 16)
        draw.text((520, 460), "CPF: 410.960.628-44", text_color, cpf_font)


        file_path = f"{user_file_name}.png"
        im.save(file_path)
        pdf = Image.open(file_path).convert("RGB")
        pdf.save(f"{user_file_name}.pdf")
        os.remove(f"{user_file_name}.png")
