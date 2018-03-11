from abc import ABC, abstractmethod


class Generator:

    def __init__(self, seed: int, a: int, c: int, m: int):
        self.listeners = []
        self.a = a
        self.c = c
        self.m = m
        self.x = seed

    # generate
    def next(self) -> int:
        self.x = (self.a * self.x + self.c) % self.m

        return self.x

    # generate an array of pseudorandom ints
    def next_N(self, n: int) -> [int]:
        rands = []

        for i in range(n):
            rands.append(self.next())

        return rands
