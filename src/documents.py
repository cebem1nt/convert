from shutil import which
from src.aconverter import Converter
import subprocess

HAS_LIBREOFFICE = which("libreoffice")
HAS_PANDOC = which("pandoc")

class Documents(Converter):
    def __init__(self, source: str, target: str):
        super().__init__(source, target)

        self.supported = [
            "odt",
            "fodt",
            "doc",
            "docx",
            "rtf",
            "html",
            "xhtml",
            "pdf",

            "ods",
            "fods",
            "xls",
            "xlsx",
            "csv",

            "odp",
            "fodp",
            "ppt",
            "pptx",
            "swf",

            "fodt",
            "ofs",
            "xml",
            "docbook",
            "uof"
        ]

    def convert(self):
        if not self.can_convert():
            raise ValueError(f"Unsupported format(s)")

        if HAS_PANDOC:
            subprocess.run(
                ["pandoc", self.source[0], "-o", self.target[0]]
            ) 

        elif HAS_LIBREOFFICE:
            filters = {
                "pdf": "draw_pdf_Export",
                "docx": "MS Word 2007 XML"
            }

            ext = self.target[1]

            if ext in filters:
                ext += ':' + filters[ext]

            subprocess.run(
                ["libreoffice", "--convert-to", ext, self.source[0]]
            )

        else:
            print("Could not convert, no backend found.")