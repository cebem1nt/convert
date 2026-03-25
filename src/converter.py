def get_extension(f: str):
    return f.split('.', maxsplit=1)[-1]

class Converter:
    def __init__(self, source: str, target: str):
        self.source = (                     # 0 - path
            source, get_extension(source)   # 1 - extension
        )
        self.target = (
            target, get_extension(target)
        )
        self.supported = ()

    def can_convert(self):
        return (self.source[1] in self.supported) and \
               (self.target[1] in self.supported)

    def convert(self):
        raise NotImplementedError()