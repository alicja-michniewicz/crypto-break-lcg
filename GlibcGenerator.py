import random

class GlibcGenerator:

    def __init__(self, seed_int:int) -> None:
        super().__init__()
        self.gen = random.glibc_prng(seed_int)

    def generate(self):
        return next(self.gen)

    def generate_n(self, n):
        return list([self.generate() for i in range(n)])