from shutil import which
from src.converter import Converter
import subprocess

# def audio_convert(file_bytes: bytes, src_format: str, target_format: str) -> bytes:
#     audio = AudioSegment.from_file(BytesIO(file_bytes), format=src_format)
#     output = BytesIO()
#     audio.export(output, format=target_format)
#     return output.getvalue()

HAS_PYDUB = True
HAS_FFMPEG = which("ffmpeg")

try:
    import AudioSegment
except:
    HAS_PYDUB = False


class Audio(Converter):
    def __init__(self, source: str, target: str):
        super().__init__(source, target)
        self.supported = (
            'wav', 'mp3', 'ogg', 'flac', 'm4a', 'aiff', 'au', 'raw', 'wma'
        )

    def convert(self):
        if not self.can_convert():
            raise ValueError(f"Unsupported format(s)")

        if HAS_FFMPEG:
            subprocess.run(
                ["ffmpeg", "-i", self.source[0], self.target[0]]
            )
            