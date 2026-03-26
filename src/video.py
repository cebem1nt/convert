from src.aconverter import Converter
from shutil import which
import subprocess

HAS_FFMPEG = which("ffmpeg")

class Video(Converter):
    def __init__(self, source: str, target: str):
        super().__init__(source, target)

        self.supported = [
            "mp4",
            "mov",
            "mkv",
            "avi",
            "flv",
            "wmv",
            "webm",
            "mpeg",
            "mpg",
            "ts",
            "m2ts",
            "3gp",
            "ogg",
            "ogv",
            "asf"
        ]

    def convert(self):
        if not self.can_convert():
            raise ValueError(f"Unsupported format(s)")

        if HAS_FFMPEG:
            subprocess.run(
                ["ffmpeg", "-hide_banner", "-loglevel", "warning", 
                    "-y", "-i", self.source[0], self.target[0]],
            )

        else:
            print("Could not convert, no backend found.")