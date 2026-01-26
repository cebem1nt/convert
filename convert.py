#!/bin/env python3
import argparse, os
import converters as conv

def main(args: argparse.Namespace):
    if not os.path.exists(args.file):
        print(f'El archivo "{args.file}" no existe')
        return

    with open(args.file, "rb") as f:
        content = f.read()

    src_format = args.file.split('.')[-1]
    base_name = args.file.rsplit('.', 1)[0]
    result = None

    try:
        match args.to:
            case "jpeg" | "png":
                result = conv.images.convert_image(content, args.to)

            case "wav" | "mp3":
                result = conv.audio.audio_convert(content, src_format, args.to)

            case "csv":
                result = conv.tables.xlsx_to_csv(content)

            case "xlsx":
                result = conv.tables.csv_to_xlsx(content)

            case _:
                print(f'El formato "{args.to}" no fue reconocido')

        with open(base_name + '.' + args.to, "wb") as f:
            f.write(result) 

    except Exception as e:
        print(f"Error: {str(e)}")
        print(f'No se pudo convertir a "{args.to}".')

if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Convertí archivos comunes sin sufrir de más."
    )
    
    p.add_argument("file", type=str, help="El archivo para convertir")
    p.add_argument("to",   type=str, help="La extensión necesaria")

    args = p.parse_args()
    
    main(args)