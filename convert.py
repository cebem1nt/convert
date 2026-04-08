#!/bin/env python3
import argparse, os, sys
from src.audio import Audio
from src.images import Image
from src.documents import Documents
from src.video import Video

converters = [Audio, Image, Documents, Video]

def get_file_name(f: str):
    tail = os.path.basename(f)
    file_name, _ =  tail.rsplit('.', 1)
    return file_name

def convert(src: str, target: str, dest: str | None):
    if not os.path.exists(src):
        sys.stderr.write(f'File "{src}" does not exist\n')
        exit(1)

    target_path = get_file_name(src)
    target_path += '.' + target

    if dest:
        target_path = os.path.join(dest, target_path)

    for Converter in converters:
        c = Converter(src, target_path)

        try:
            if c.can_convert(): c.convert(); break

        except KeyboardInterrupt:
            sys.stderr.write("Conversion was interrupted!\n")
            exit(1)
    else:
        print(f"Could not convert \"{src}\" to \".{target}\", unsupported extension(s)")

def main(args: argparse.Namespace):
    args.target = args.target.lstrip('.') # strip optional .

    if args.dest:
        os.makedirs(args.dest, exist_ok=True)

    sources = args.sources

    for src in sources:
        print(src)

        if os.path.isdir(src):
            files = os.listdir(src)
            sources += [os.path.join(src, f) for f in files]
            continue
    
        convert(src, args.target, args.dest)

    return 0


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Convert files to different file types"
    )
    
    p.add_argument("sources",      type=str, nargs="*", help="Source file[s]")
    p.add_argument("target",       type=str,            help="Target extension")
    p.add_argument("-d", "--dest", type=str,            help="Destination directory")

    args = p.parse_args()
    
    exit(main(args))