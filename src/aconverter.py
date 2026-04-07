def get_file_extension(f: str):
    return f.rsplit('.', maxsplit=1)[-1]

class Converter:
    def __init__(self, source: str, target: str):
        self.source = (                          # 0 - path
            source, get_file_extension(source)   # 1 - extension
        )
        self.target = (
            target, get_file_extension(target)
        )
        self.supported = []

    def can_convert(self):
        return (self.source[1] in self.supported) and \
               (self.target[1] in self.supported)

    def convert(self):
        raise NotImplementedError()