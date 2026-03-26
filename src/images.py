from shutil import which
from src.aconverter import Converter
import subprocess

HAS_PIL = True
HAS_FFMPEG = which("ffmpeg")

try:
    from PIL import Image
except:
    HAS_PIL = False

class Image(Converter):
    def __init__(self, source: str, target: str):
        super().__init__(source, target)

        self.supported = [
            "bmp", "jpg", "jpeg", "png", "tif", "tiff", "webp", "ppm", "pgm", "pbm", "pnm", "tga", "exr", "ico", "heif", "heic", "avif", "jpg2000", "pcx", "psd"
        ]

        if HAS_FFMPEG:
            self.supported += ["rgb", "rgba", "yuv", "cin", "dpx", "pam", "svg"]

    def convert(self):
        if not self.can_convert():
            raise ValueError(f"Unsupported format(s)")

        if HAS_FFMPEG:
            subprocess.run(
                ["ffmpeg", "-y", "-i", self.source[0], self.target[0]],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

        elif HAS_PIL:
            img = Image.open(self.source[0])
            img.save(self.target[0], format=self.target[1].upper())

        else:
            print("Could not convert, no backend found.")