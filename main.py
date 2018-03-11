from GlibcGenerator import GlibcGenerator
from generator import Generator
from libc_predictor import GlibcPredictor
from predictor import Predictor

TESTS = 10000

# X_0 = seed
# X_i = (aX_(i-1) + c) mod m
TEST_SEED = 5
TEST_A = 11
TEST_C = 3
TEST_M = 8259

TEST_GLIBC_SEED = 1

#
# print(gen.a)
# print(gen.next())



def test_1(n:int):
    gen = Generator(TEST_SEED, TEST_A, TEST_C, TEST_M)
    predictor = Predictor(gen)

    success = 0

    for i in range(n):
        prediction = predictor.predict_next()
        generated = gen.next()

        if generated == prediction:
            success+=1

    print("LCG prediction prob. {}".format(success/n))

def test_2(n:int):
    gen = GlibcGenerator(TEST_GLIBC_SEED)
    predictor = GlibcPredictor(gen)

    success = 0

    for i in range(n):
        prediction = predictor.predict()
        generated = gen.generate()

        print("Glibc pred {}".format(prediction))
        print("Glibc real {}".format(generated))

        if generated == prediction:
            success += 1

    print("Glibc prediction prob. {}".format(success/n))


test_1(100)

test_2(1000)