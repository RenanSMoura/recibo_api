import textwrap

from PIL import Image, ImageDraw, ImageFont

from app.gen.doc.repository import TicketPDFRepository
from app.gen.model import Ticket
from app.gen.utils.os_helper import OSHelper
from repository.configs import BASE_FILE_NAME, INITIAL_INDENT, TEXT_COLOR, TEXT_FONT_FAMILY, TEXT_FONT_SIZE, CPF


class TickedPDFImpl(TicketPDFRepository):

    def __init__(self, ticket: Ticket):
        self._ticket = ticket
        self._text_color = TEXT_COLOR
        self._text_font = ImageFont.truetype(TEXT_FONT_FAMILY, TEXT_FONT_SIZE)
        self.os_helper = OSHelper()

    def generate_ticket(self):
        self._generate_new_image()
        self._draw_image()

        text_formatted = self._format_text_to_append()

        self._append_text_into_image(text_formatted)
        self._append_session_payment_date()
        self._append_cpf_document()
        self._process_file()

    def _generate_new_image(self):
        self.img = Image.open(BASE_FILE_NAME)

    def _draw_image(self):
        self.draw_img = ImageDraw.Draw(self.img)

    def _format_text_to_append(self):
        formatted_text = ""
        width = 75
        description = self._ticket.final_text
        lines = textwrap.wrap(description, width, initial_indent=INITIAL_INDENT)
        for idx, line in enumerate(lines):
            line += str('\n')
            formatted_text += line

        return formatted_text

    def _append_text_into_image(self, text):
        position_in_pixels = (120, 165)
        text_spacing = 15
        self.draw_img.multiline_text(
            position_in_pixels,
            text,
            self._text_color,
            self._text_font,
            spacing=text_spacing)

    def _append_session_payment_date(self):
        date = self._ticket.get_payment_date()
        position_in_pixels = (150, 320)
        self.draw_img.text(position_in_pixels, date, self._text_color, self._text_font)

    def _append_cpf_document(self):
        position_in_pixels = (520, 320)
        self.draw_img.text(position_in_pixels, CPF, self._text_color, self._text_font)

    def _process_file(self):
        file_name = self._ticket.get_file_name()

        file_name_path = f"{file_name}.png"
        file_name_pdf = f"{file_name}.pdf"
        
        self.os_helper.process_folder_creation(file_name)

        self._process_file_and_save(file_name_path)
        
        self.os_helper.create_pdf_file(
            file_name=file_name_pdf,
            file_path=file_name_path
        )

        self.os_helper.delete_file(file_name_path)

    def _process_file_and_save(self, file_name):
        self.img.save(file_name)
