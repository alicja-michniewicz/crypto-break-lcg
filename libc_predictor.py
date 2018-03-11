from GlibcGenerator import GlibcGenerator

class GlibcPredictor:

    def __init__(self, generator: GlibcGenerator) -> None:
        super().__init__()
        self.gen = generator


    def predict(self):
        results = self.gen.generate_n(32)

        modulus = 2**31
        print(modulus)
        print(1<<32)

        #75% szans na to
        o32 = (results[1] + results[29]) % modulus
        return o32