#!/bin/env python3
import argparse, os, sys
from src.audio import Audio

converters = [Audio]

def main(args: argparse.Namespace):
    if not os.path.exists(args.source):
        sys.stderr.write(f'File "{args.source}" does not exist\n')
        return 1

    target_file = args.source.rsplit('.', 1)[0]
    target_file += '.' + args.target

    for Converter in converters:
        c = Converter(args.source, target_file)

        if c.can_convert():
            return c.convert()

    return 0


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Convertí archivos comunes sin sufrir de más."
    )
    
    p.add_argument("source",  type=str, help="Source file")
    p.add_argument("target",  type=str, help="Target extension")

    args = p.parse_args()
    
    exit(main(args))