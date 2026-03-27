# Convert

A python wrapper script or a _swiss knife_ to convert between different file extensions

### Supported file types:

- Audio
- Documents
- Images
- Video

### Supported backends

To use this, install any of the following applications/libs:

- [ffmpeg](https://github.com/FFmpeg/FFmpeg): Audio/video/image support
- [Pydub](github.com/jiaaro/pydub): Audio support
- [Pillow](https://pypi.org/project/pillow/): Image support
- [libreoffice](https://www.libreoffice.org/): document support
- [pandoc](https://github.com/jgm/pandoc): document support

## Usage

Just run script, provide file you want to convert and a target extension

```sh
python convert.py file.mp4 mov
# Or any documents type
python convert.py file.docx pdf 
# Or audio
python convert.py file.flac mp3 
```

## How does it work? 

Scipt checks the file type provided, finds matching global handler and based on the programs you have installed, converts to a target file extension. The script itself does not implement any file parsing / conversion.

## It does not work?

This script definitely has bugs, feel free to contribute or submit an issue 