from shutil import which
from src.aconverter import Converter
from typing import Optional

import subprocess, os

HAS_PYDUB = True
HAS_FFMPEG = which("ffmpeg")

try:
    from pydub import AudioSegment
except:
    HAS_PYDUB = False


class Audio(Converter):
    def __init__(self, source: str, target: str):
        super().__init__(source, target)

        self.supported = [
            'wav', 'mp3', 'ogg', 'flac', 'm4a', 'aiff', 'au', 'raw', 'wma'
        ]

        if HAS_FFMPEG:
            self.supported += ['aac', 'ac3', 'alac', 'amr', 'dts', 'opus', 'pcm']

    def convert(self):
        if not self.can_convert():
            raise ValueError(f"Unsupported format(s)")

        if HAS_FFMPEG:
            subprocess.run(
                ["ffmpeg", "-y", "-i", self.source[0], self.target[0]],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

        elif HAS_PYDUB:
            segment = AudioSegment.from_file(self.source[0])
            segment.export(self.target[0], self.target[1])

        else:
            print("Could not convert, no backend found.")